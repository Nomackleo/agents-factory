#!/usr/bin/env python3
import re
import sys
import os

def validate_markdown(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    errors = []

    # Check for the 5 W's in the document (heuristic: just check if the words exist for now)
    w_words = ['who', 'what', 'when', 'where', 'why', 'quien', 'quién', 'qué', 'que', 'cuando', 'cuándo', 'donde', 'dónde', 'por qué', 'por que']
    found_ws = [w for w in w_words if w.lower() in content.lower()]
    
    # We expect at least some of these to be addressed explicitly in a well-formed docs-as-code output
    if len(found_ws) < 3:
        errors.append("Fallo Validación: El documento no parece abordar claramente las 5 W's (WHO, WHAT, WHEN, WHERE, WHY).")

    # Check for kebab-case filenames
    filename = os.path.basename(file_path)
    if not re.match(r'^[a-z0-9\-]+\.md$', filename):
        errors.append(f"Fallo Taxonomía: El nombre del archivo '{filename}' no cumple con 'kebab-case'.")

    if errors:
        print(f"Errores en {filename}:")
        for error in errors:
            print(f" - {error}")
        sys.exit(1)
    else:
        print(f"Validación exitosa para {filename}. Cumple con los estándares de Docs-as-Code.")
        sys.exit(0)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python docs-validator.py <archivo.md>")
        sys.exit(1)
    
    validate_markdown(sys.argv[1])
