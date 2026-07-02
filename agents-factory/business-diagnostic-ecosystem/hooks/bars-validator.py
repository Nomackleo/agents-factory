#!/usr/bin/env python3
import re
import sys
import os

def validate_bars_usage(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    errors = []
    filename = os.path.basename(file_path)

    # 1. Validar que no se usen escalas Likert abstractas
    abstract_likert_patterns = [
        r'1 a 5 donde 1 es',
        r'Totalmente en desacuerdo',
        r'Muy en desacuerdo',
        r'Totalmente de acuerdo'
    ]
    
    for pattern in abstract_likert_patterns:
        if re.search(pattern, content, re.IGNORECASE):
            errors.append(f"Fallo Psicométrico: Se detectó una escala Likert abstracta o subjetiva ('{pattern}').")

    # 2. Validar presencia de BARS (Behaviorally Anchored Rating Scales)
    # Buscamos la estructura definida en diagnostic.md: [Nivel X - Nombre]: "Descriptor de conducta..."
    bars_pattern = r'\[Nivel [1-5].*?\]:\s*["\'][^"\']+["\']'
    bars_matches = re.findall(bars_pattern, content)
    
    if len(bars_matches) < 2 and 'SKILL' not in filename: # Si es un test generado o un skill
        errors.append("Fallo Metodológico: El documento carece de descriptores de conducta anclados (BARS). Las puntuaciones numéricas deben estar atadas a una evidencia conductual explícita.")

    # 3. Validar prohibición de Double-barreled questions
    # Busca preguntas con múltiples conectores " y " o " o " que evalúan dos cosas.
    double_barrel_pattern = r'\¿[^?]+ y [^?]+\?'
    double_barrels = re.findall(double_barrel_pattern, content)
    if len(double_barrels) > 0:
        errors.append(f"Fallo Estructural: Posibles 'double-barreled questions' detectadas (ej. {double_barrels[0]}). Una pregunta solo debe evaluar un constructo a la vez.")

    if errors:
        print(f"Errores de diagnóstico en {filename}:")
        for error in errors:
            print(f" - {error}")
        print("\nResolución: Reestructura el test usando BARS e ítems monotemáticos.")
        sys.exit(1)
    else:
        print(f"Validación psicométrica exitosa para {filename}.")
        sys.exit(0)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python bars-validator.py <archivo.md>")
        sys.exit(1)
    
    validate_bars_usage(sys.argv[1])
