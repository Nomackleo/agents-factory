#!/usr/bin/env python3
import re
import sys
import os

def validate_executive_markdown(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    errors = []

    # Validar formato kebab-case
    filename = os.path.basename(file_path)
    if not re.match(r'^[a-z0-9\-]+\.md$', filename):
        errors.append(f"Fallo Taxonomía: El nombre '{filename}' no cumple con 'kebab-case'.")

    # Validar que no haya exceso de jerga técnica si es un documento ejecutivo puro
    technical_jargon = ['api', 'endpoint', 'json', 'sql', 'microservicios', 'kubernetes', 'docker']
    found_jargon = [j for j in technical_jargon if j.lower() in content.lower()]
    
    if len(found_jargon) > 3:
        errors.append(f"Fallo de Tono: Se detectó jerga técnica en un documento ejecutivo ({', '.join(found_jargon)}). Revisar si es pertinente.")

    # Validar elementos clave ejecutivos (dependiendo del tipo de doc, pero generalizando)
    executive_keywords = ['objetivo', 'meta', 'kpi', 'okr', 'riesgo', 'presupuesto', 'roi', 'estrategia', 'impacto']
    found_exec = [e for e in executive_keywords if e.lower() in content.lower()]
    if len(found_exec) == 0:
        errors.append("Fallo Estructural: El documento carece de vocabulario de impacto ejecutivo o estratégico (Faltan menciones a KPIs, riesgos, objetivos, etc).")

    if errors:
        print(f"Errores en {filename}:")
        for error in errors:
            print(f" - {error}")
        sys.exit(1)
    else:
        print(f"Validación exitosa para {filename}. Cumple con los estándares de Docs-as-Code Executive.")
        sys.exit(0)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python executive-validator.py <archivo.md>")
        sys.exit(1)
    
    validate_executive_markdown(sys.argv[1])
