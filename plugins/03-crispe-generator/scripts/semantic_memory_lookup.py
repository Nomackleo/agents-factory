#!/usr/bin/env python3
"""
Semantic Memory Lookup - Codebase-Memory-MCP (SQLite FTS5 & Domain Taxonomy)

Consulta la base de datos relacional/indexada de Antigravity (mcp/codebase-memory-mcp/data/codebase_memory.sqlite)
para determinar si una tarea requerida coincide con ecosistemas, áreas corporativas o skills existentes.

Protocolo de Decisión (Token Economy & DRY Agéntico):
- ATTACH_SKILL: Si se encuentra un ecosistema relevante en la memoria, sugiere adjuntar un nuevo SKILL.md a dicho ecosistema dentro de su División Corporativa.
- CREATE_ECOSYSTEM: Si no hay coincidencia funcional aceptable, sugiere aprovisionar un nuevo Ecosistema agéntico.
"""

import os
import sys
import sqlite3
import re
from typing import Dict, Any, List, Tuple

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PLUGIN_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, '..'))
WORKSPACE_ROOT = os.path.abspath(os.path.join(PLUGIN_ROOT, '..', '..'))
DB_PATH = os.path.join(WORKSPACE_ROOT, 'mcp', 'codebase-memory-mcp', 'data', 'codebase_memory.sqlite')


def get_db_connection() -> sqlite3.Connection:
    if not os.path.exists(DB_PATH):
        raise FileNotFoundError(f"Base de datos no encontrada en: {DB_PATH}")
    return sqlite3.connect(DB_PATH)


def lookup_memory(query: str) -> Dict[str, Any]:
    """
    Busca coincidencias relacionales/lexicales en la tabla codebase_index.
    Calcula un score de relevancia basado en términos clave, coincidencia de dominio y ecosistema.
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    # Normalizar términos de búsqueda
    raw_tokens = re.findall(r'\w+', query.lower())
    # Filtrar palabras vacías comunes y términos de arquitectura genéricos
    stopwords = {
        'de', 'la', 'el', 'en', 'y', 'a', 'los', 'del', 'se', 'las', 'por', 'un', 'para', 'con', 'no', 'una', 
        'su', 'al', 'lo', 'como', 'querría', 'crear', 'un', 'agente', 'que', 'haga', 'sistema', 'agéntico', 
        'ecosistema', 'desarrollar', 'construir', 'implementar', 'nuevo', 'para', 'área', 'división'
    }
    keywords = [t for t in raw_tokens if t not in stopwords and len(t) > 2]

    if not keywords:
        keywords = raw_tokens

    # Consultar ecosistemas existentes, dominios y sus descripciones
    cursor.execute("""
        SELECT ecosystem, description, file_path, domain_id, domain_name 
        FROM codebase_index 
        WHERE ecosystem NOT LIKE 'project:%' AND ecosystem NOT LIKE 'domain:%'
    """)
    rows = cursor.fetchall()

    ecosystem_scores: Dict[str, Dict[str, Any]] = {}

    for eco, desc, path, dom_id, dom_name in rows:
        if eco not in ecosystem_scores:
            ecosystem_scores[eco] = {
                "ecosystem": eco,
                "domain_id": dom_id or "01_executive_governance",
                "domain_name": dom_name or "Strategy & Executive Governance",
                "score": 0,
                "matched_terms": set(),
                "file_count": 0,
                "sample_files": []
            }
        
        eco_data = ecosystem_scores[eco]
        eco_data["file_count"] += 1

        text_to_search = f"{eco} {desc} {path} {dom_id} {dom_name}".lower()
        for kw in keywords:
            if kw in text_to_search:
                # Ponderación superior si la coincidencia ocurre en el nombre del ecosistema, dominio o skill
                weight = 5 if (kw in eco.lower() or "skill.md" in path.lower() or kw in (dom_name or '').lower()) else 1
                eco_data["score"] += weight
                eco_data["matched_terms"].add(kw)
                if len(eco_data["sample_files"]) < 3 and ("SKILL.md" in path or "README.md" in path):
                    eco_data["sample_files"].append(path)

    # Ordenar por diversidad de términos coincidentes y puntuación total
    sorted_ecosystems = sorted(
        ecosystem_scores.values(), 
        key=lambda x: (len(x["matched_terms"]), x["score"]), 
        reverse=True
    )

    top_match = sorted_ecosystems[0] if sorted_ecosystems else None
    
    # Umbral de coincidencia aceptable para adjuntar skill vs crear ecosistema
    if top_match and top_match["score"] >= 2:
        decision = "ATTACH_SKILL"
        rationale = f"Se encontró coincidencia relevante con el ecosistema '{top_match['ecosystem']}' en la División '[{top_match['domain_name']}]' (Score: {top_match['score']}, Coincidencias: {list(top_match['matched_terms'])})."
        target_ecosystem = top_match["ecosystem"]
        target_domain = top_match["domain_name"]
    else:
        decision = "CREATE_ECOSYSTEM"
        rationale = "No se encontró un ecosistema existente con suficiente coincidencia de dominio. Se sugiere crear un nuevo Ecosistema."
        target_ecosystem = None
        target_domain = None

    return {
        "query": query,
        "keywords": keywords,
        "decision": decision,
        "rationale": rationale,
        "target_ecosystem": target_ecosystem,
        "target_domain": target_domain,
        "top_matches": [
            {
                "ecosystem": m["ecosystem"],
                "domain_name": m["domain_name"],
                "score": m["score"],
                "matched_terms": list(m["matched_terms"])
            } for m in sorted_ecosystems[:4] if m["score"] > 0
        ]
    }


def main():
    if len(sys.argv) < 2:
        print("Uso: python semantic_memory_lookup.py <query_o_prompt_requerido>")
        sys.exit(1)

    user_query = " ".join(sys.argv[1:])
    result = lookup_memory(user_query)

    print("\n--- RESULTADO DE BÚSQUEDA EN MEMORIA PERSISTENTE (SQLite) ---")
    print(f"Decisión: {result['decision']}")
    print(f"Ecosistema Objetivo: {result['target_ecosystem']}")
    if result['target_domain']:
        print(f"División Corporativa: {result['target_domain']}")
    print(f"Justificación: {result['rationale']}")
    if result['top_matches']:
        print("Top Ecosistemas Coincidentes por División:")
        for m in result['top_matches']:
            print(f"  - [{m['domain_name']}] {m['ecosystem']} (Score: {m['score']}, Términos: {m['matched_terms']})")
    print("-----------------------------------------------------------\n")


if __name__ == '__main__':
    main()
