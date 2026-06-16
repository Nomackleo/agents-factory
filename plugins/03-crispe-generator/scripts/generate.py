#!/usr/bin/env python3
import sys
import os

def generate_prompt(role, context, task, format_str):
    """
    Lee el template base Neo-CRISPE y reemplaza los tokens.
    Garantiza que la salida sea estrictamente el prompt listo para inyectar en otro agente.
    """
    template_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'crispe-high-performance.md')
    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            template = f.read()
            
        prompt = template.replace('{{role_definition}}', role)
        prompt = prompt.replace('{{business_context}}', context)
        prompt = prompt.replace('{{exact_task}}', task)
        prompt = prompt.replace('{{specific_constraint}}', 'Must comply with ISO/SOC2 standards of the workspace.')
        prompt = prompt.replace('{{output_format}}', format_str)
        prompt = prompt.replace('{{example_input}}', 'Task input')
        prompt = prompt.replace('{{example_output}}', 'Strict output following format')
        
        return prompt
    except FileNotFoundError:
        return "Error: Template crispe-high-performance.md no encontrado."

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage: generate.py <role> <context> <task> <format>")
        sys.exit(1)
        
    final_prompt = generate_prompt(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    print(final_prompt)
