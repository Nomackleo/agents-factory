#!/usr/bin/env python3
"""
Graphify Indexer - Ingesta Automática del Ecosistema Agéntico
Recorre la estructura de agents-factory y puebla el Codebase-Memory-MCP (SQLite)
con relaciones jerárquicas padre-hijo para la navegación de los agentes.
"""
import os
import sqlite3
import re

# Rutas principales
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, '..'))
AGENTS_FACTORY_DIR = os.path.join(PROJECT_ROOT, 'agents-factory')
DB_PATH = os.path.join(PROJECT_ROOT, 'mcp', 'codebase-memory-mcp', 'data', 'codebase_memory.sqlite')

def get_db_connection():
    if not os.path.exists(DB_PATH):
        raise FileNotFoundError(f"No se encontró la base de datos en {DB_PATH}. Por favor, inicializa el MCP primero.")
    return sqlite3.connect(DB_PATH)

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

def index_file(cursor, file_path, ecosystem, description):
    """Inserta o actualiza un archivo en la base de datos y retorna su ruta relativa."""
    # Convertir a ruta relativa desde la raíz del proyecto para mantener uniformidad de tokens
    rel_path = os.path.relpath(file_path, PROJECT_ROOT).replace('\\', '/')
    cursor.execute('''
        INSERT INTO codebase_index (file_path, ecosystem, description) 
        VALUES (?, ?, ?) 
        ON CONFLICT(file_path) 
        DO UPDATE SET description=excluded.description, last_updated=CURRENT_TIMESTAMP
    ''', (rel_path, ecosystem, description))
    return rel_path

def add_relation(cursor, source, target, relation_type):
    """Añade una relación al grafo relacional."""
    cursor.execute('''
        INSERT OR IGNORE INTO file_relations (source_file, target_file, relation_type) 
        VALUES (?, ?, ?)
    ''', (source, target, relation_type))

def crawl_and_index():
    print("Iniciando indexador automático (Graphify Indexer)...")
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Limpiar tabla de relaciones para arrancar limpios en cada corrida completa (útil en dev)
    cursor.execute("DELETE FROM file_relations")
    
    ecosystems_found = 0
    files_indexed = 0
    
    for item in os.listdir(AGENTS_FACTORY_DIR):
        ecosystem_dir = os.path.join(AGENTS_FACTORY_DIR, item)
        readme_path = os.path.join(ecosystem_dir, 'README.md')
        
        # Un ecosistema es un directorio que contiene un README.md
        if os.path.isdir(ecosystem_dir) and os.path.exists(readme_path):
            ecosystem_name = item
            desc = extract_what_from_readme(readme_path)
            
            ecosystem_rel_path = index_file(cursor, readme_path, ecosystem_name, f"Ecosistema Padre: {desc}")
            ecosystems_found += 1
            
            # Recorrer recursivamente archivos internos
            for root, dirs, files in os.walk(ecosystem_dir):
                for f in files:
                    if f == "README.md" and root == ecosystem_dir:
                        continue # El README padre ya fue indexado
                    
                    file_path = os.path.join(root, f)
                    rel_dir = os.path.relpath(root, ecosystem_dir).replace('\\', '/')
                    
                    file_desc = f"Componente agéntico ({rel_dir}) del ecosistema {ecosystem_name}"
                    file_rel_path = index_file(cursor, file_path, ecosystem_name, file_desc)
                    files_indexed += 1
                    
                    # Agregar relación jerárquica (Padre -> Hijo)
                    add_relation(cursor, ecosystem_rel_path, file_rel_path, "CONTAINS")
                    
    conn.commit()
    conn.close()
    
    print("=====================================================")
    print("[EXITO] Indexación completada en Codebase-Memory-MCP.")
    print(f"        Ecosistemas procesados: {ecosystems_found}")
    print(f"        Componentes internos indexados: {files_indexed}")
    print("=====================================================")

if __name__ == "__main__":
    crawl_and_index()
