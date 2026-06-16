#!/usr/bin/env python3
import json
import sys

def validate_handoff(filepath):
    """
    Valida que el payload entre agentes cumpla con el esquema JSON mínimo.
    Esto minimiza el Change Failure Rate (Métrica DORA).
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            required_keys = {"source_agent", "target_agent", "payload"}
            if not required_keys.issubset(data.keys()):
                print("Error: Invalid schema. Missing required fields: source_agent, target_agent, payload.")
                sys.exit(1)
            print("Handoff payload valid.")
            sys.exit(0)
    except Exception as e:
        print(f"Error reading or parsing handoff file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: handoff-validator.py <path_to_json_payload>")
        sys.exit(1)
    validate_handoff(sys.argv[1])
