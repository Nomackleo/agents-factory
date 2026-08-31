#!/usr/bin/env python3
"""
Graphify Indexer - Ingesta Automática del Ecosistema Agéntico y Dominios Corporativos
Recorre la estructura de agents-factory y projects/ y puebla el Codebase-Memory-MCP (SQLite)
con categorización por Áreas Corporativas (Dominios), relaciones jerárquicas padre-hijo
y grafo relacional completo para la navegación determinista de los agentes.
"""
import os
import json
import sqlite3
import re

# Rutas principales
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, '..'))
AGENTS_FACTORY_DIR = os.path.join(PROJECT_ROOT, 'agents-factory')
DOMAIN_MANIFEST_PATH = os.path.join(AGENTS_FACTORY_DIR, 'domain_manifest.json')
DB_PATH = os.path.join(PROJECT_ROOT, 'mcp', 'codebase-memory-mcp', 'data', 'codebase_memory.sqlite')

def get_db_connection():
    if not os.path.exists(DB_PATH):
        raise FileNotFoundError(f"No se encontró la base de datos en {DB_PATH}. Por favor, inicializa el MCP primero.")
    return sqlite3.connect(DB_PATH)

def ensure_schema_compatibility(cursor):
    """Asegura que la tabla codebase_index tenga las columnas domain_id y domain_name."""
    cursor.execute("PRAGMA table_info(codebase_index)")
    columns = [col[1] for col in cursor.fetchall()]
    
    if "domain_id" not in columns:
        cursor.execute("ALTER TABLE codebase_index ADD COLUMN domain_id TEXT DEFAULT 'unassigned'")
    if "domain_name" not in columns:
        cursor.execute("ALTER TABLE codebase_index ADD COLUMN domain_name TEXT DEFAULT 'General Domain'")

def load_domain_mapping():
    """Carga el mapa de ecosistemas a dominios desde domain_manifest.json."""
    mapping = {}
    domain_info = {}
    
    if os.path.exists(DOMAIN_MANIFEST_PATH):
        try:
            with open(DOMAIN_MANIFEST_PATH, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for dom in data.get("domains", []):
                    dom_id = dom.get("id")
                    dom_name = dom.get("name")
                    domain_info[dom_id] = {
                        "name": dom_name,
                        "description": dom.get("description", ""),
                        "leader": dom.get("leader_role", "")
                    }
                    for eco in dom.get("ecosystems", []):
                        mapping[eco] = (dom_id, dom_name)
        except Exception as e:
            print(f"[ADVERTENCIA] Error leyendo domain_manifest.json: {e}")
            
    return mapping, domain_info

def extract_what_from_readme(filepath):
    """Extrae la misión (WHAT) del README.md de un ecosistema."""
    if not os.path.exists(filepath):
        return "Sin descripción"
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        match = re.search(r'\*\*WHAT\*\*:\s*(.*)', content)
        if match:
            return match.group(1).strip()
    return "Ecosistema agéntico (Sin descripción explícita de WHAT)"

def index_file(cursor, file_path, ecosystem, description, domain_id="general", domain_name="General Domain"):
    """Inserta o actualiza un archivo en la base de datos con su dominio y retorna su ruta relativa."""
    rel_path = os.path.relpath(file_path, PROJECT_ROOT).replace('\\', '/')
    cursor.execute('''
        INSERT INTO codebase_index (file_path, ecosystem, description, domain_id, domain_name) 
        VALUES (?, ?, ?, ?, ?) 
        ON CONFLICT(file_path) 
        DO UPDATE SET 
            description=excluded.description, 
            ecosystem=excluded.ecosystem,
            domain_id=excluded.domain_id,
            domain_name=excluded.domain_name,
            last_updated=CURRENT_TIMESTAMP
    ''', (rel_path, ecosystem, description, domain_id, domain_name))
    return rel_path

def add_relation(cursor, source, target, relation_type):
    """Añade una relación al grafo relacional."""
    cursor.execute('''
        INSERT OR IGNORE INTO file_relations (source_file, target_file, relation_type) 
        VALUES (?, ?, ?)
    ''', (source, target, relation_type))

def crawl_and_index():
    print("Iniciando indexador automático por Dominios (Graphify Enterprise Indexer)...")
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # 1. Asegurar columnas de dominio en el esquema
    ensure_schema_compatibility(cursor)
    
    # 2. Cargar mapeo de dominios
    eco_to_domain, domain_info = load_domain_mapping()
    
    # Limpiar tabla de relaciones para consistencia
    cursor.execute("DELETE FROM file_relations")
    
    domains_processed = len(domain_info)
    ecosystems_found = 0
    projects_found = 0
    files_indexed = 0
    
    # 3. Indexar Nodos Raíz de Dominio
    for dom_id, d_data in domain_info.items():
        dom_node_path = f"domains/{dom_id}"
        dom_desc = f"División Corporativa: {d_data['name']} (Líder: {d_data['leader']}) - {d_data['description']}"
        cursor.execute('''
            INSERT INTO codebase_index (file_path, ecosystem, description, domain_id, domain_name)
            VALUES (?, ?, ?, ?, ?)
            ON CONFLICT(file_path)
            DO UPDATE SET description=excluded.description, domain_name=excluded.domain_name, last_updated=CURRENT_TIMESTAMP
        ''', (dom_node_path, f"domain:{dom_id}", dom_desc, dom_id, d_data['name']))
        files_indexed += 1
    
    # 4. Indexar Ecosistemas Agénticos Reutilizables (agents-factory/)
    if os.path.exists(AGENTS_FACTORY_DIR):
        for item in os.listdir(AGENTS_FACTORY_DIR):
            ecosystem_dir = os.path.join(AGENTS_FACTORY_DIR, item)
            readme_path = os.path.join(ecosystem_dir, 'README.md')
            
            if os.path.isdir(ecosystem_dir) and os.path.exists(readme_path):
                ecosystem_name = item
                desc = extract_what_from_readme(readme_path)
                
                # Obtener Dominio Asignado
                domain_id, domain_name = eco_to_domain.get(
                    ecosystem_name, 
                    ("01_executive_governance", "Strategy & Executive Governance")
                )
                
                ecosystem_rel_path = index_file(
                    cursor, readme_path, ecosystem_name, 
                    f"Ecosistema Padre: {desc}", domain_id, domain_name
                )
                ecosystems_found += 1
                
                # Relacionar Dominio ➔ Ecosistema
                dom_node_path = f"domains/{domain_id}"
                add_relation(cursor, dom_node_path, ecosystem_rel_path, "DOMAIN_OWNS_ECOSYSTEM")
                
                for root, dirs, files in os.walk(ecosystem_dir):
                    for f in files:
                        if f == "README.md" and root == ecosystem_dir:
                            continue
                        
                        file_path = os.path.join(root, f)
                        rel_dir = os.path.relpath(root, ecosystem_dir).replace('\\', '/')
                        
                        file_desc = f"Componente agéntico ({rel_dir}) de {ecosystem_name} [{domain_name}]"
                        file_rel_path = index_file(
                            cursor, file_path, ecosystem_name, 
                            file_desc, domain_id, domain_name
                        )
                        files_indexed += 1
                        
                        add_relation(cursor, ecosystem_rel_path, file_rel_path, "CONTAINS")

    # 5. Indexar Proyectos Corporativos Independientes (projects/)
    projects_dir = os.path.join(PROJECT_ROOT, 'projects')
    if os.path.exists(projects_dir):
        for item in os.listdir(projects_dir):
            proj_path = os.path.join(projects_dir, item)
            if os.path.isdir(proj_path):
                proj_name = f"project:{item}"
                proj_domain_id = "projects_execution"
                proj_domain_name = "Project Execution & Client Delivery"
                projects_found += 1
                
                for root, dirs, files in os.walk(proj_path):
                    for f in files:
                        if f.startswith('.'):
                            continue
                        file_path = os.path.join(root, f)
                        rel_dir = os.path.relpath(root, proj_path).replace('\\', '/')
                        file_desc = f"Artefacto de entrega ({rel_dir}) del proyecto {item}"
                        file_rel_path = index_file(
                            cursor, file_path, proj_name, 
                            file_desc, proj_domain_id, proj_domain_name
                        )
                        files_indexed += 1

    conn.commit()
    conn.close()
    
    print("=====================================================")
    print("[EXITO] Indexación Enterprise completada en Codebase-Memory-MCP (SQLite).")
    print(f"        Divisiones Corporativas (Dominios): {domains_processed}")
    print(f"        Ecosistemas procesados: {ecosystems_found}")
    print(f"        Proyectos independientes indexados: {projects_found}")
    print(f"        Componentes y entregables indexados: {files_indexed}")
    print("=====================================================")

if __name__ == "__main__":
    crawl_and_index()
