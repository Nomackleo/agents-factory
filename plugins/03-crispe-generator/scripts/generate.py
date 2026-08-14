#!/usr/bin/env python3
"""
Neo-CRISPE v2.0 Builder Generator Script
Integrado con consulta a memoria relacional SQLite (Codebase-Memory-MCP).
"""

import sys
import os
import re
from semantic_memory_lookup import lookup_memory

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_PATH = os.path.join(SCRIPT_DIR, '..', 'assets', 'crispe-high-performance.md')
WORKSPACE_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, '..', '..', '..'))
AGENTS_FACTORY_DIR = os.path.join(WORKSPACE_ROOT, 'agents-factory')


def sanitize_kebab(text: str) -> str:
    """Convierte una cadena a formato kebab-case estricto."""
    text = text.lower().strip()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    return text.strip('-')


def generate_crispe_skill(
    role: str, 
    context: str, 
    task: str, 
    format_str: str = "xml", 
    skill_name: str = None, 
    write_file: bool = False
) -> str:
    """
    Renderiza el template base Neo-CRISPE v2.0 y opcionalmente escribe el activo SKILL.md.
    """
    if not os.path.exists(TEMPLATE_PATH):
        return "Error: Plantilla crispe-high-performance.md no encontrada."

    with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
        template = f.read()

    # Búsqueda previa en memoria SQLite
    query = f"{role} {context} {task}"
    memory_res = lookup_memory(query)
    
    clean_skill_name = sanitize_kebab(skill_name) if skill_name else sanitize_kebab(role)
    skill_desc = f"Skill especializado en {task} dentro del framework Antigravity."

    prompt = template.replace('{{skill_name}}', clean_skill_name)
    prompt = prompt.replace('{{skill_description}}', skill_desc)
    prompt = prompt.replace('{{role_definition}}', role)
    prompt = prompt.replace('{{business_context}}', context)
    prompt = prompt.replace('{{exact_task}}', task)
    prompt = prompt.replace('{{specific_constraint}}', 'Must comply strictly with ISO 25010 / SOC 2 / DORA corporate standards.')
    prompt = prompt.replace('{{output_format}}', format_str)
    prompt = prompt.replace('{{example_input}}', 'User input task payload')
    prompt = prompt.replace('{{example_output}}', 'Validated output complying 100% with requirements')

    if write_file:
        decision = memory_res["decision"]
        target_eco = memory_res["target_ecosystem"]

        if decision == "ATTACH_SKILL" and target_eco:
            target_dir = os.path.join(AGENTS_FACTORY_DIR, target_eco, '.agents', 'skills', clean_skill_name)
        else:
            new_eco_name = f"{clean_skill_name}-ecosystem"
            target_dir = os.path.join(AGENTS_FACTORY_DIR, new_eco_name, '.agents', 'skills', clean_skill_name)
            # Asegurar directorio de ecosistema
            os.makedirs(os.path.join(AGENTS_FACTORY_DIR, new_eco_name), exist_ok=True)

        os.makedirs(target_dir, exist_ok=True)
        skill_file_path = os.path.join(target_dir, 'SKILL.md')

        with open(skill_file_path, 'w', encoding='utf-8') as f_out:
            f_out.write(prompt)
            
        print(f"\n[ÉXITO] Artefacto Neo-CRISPE generado en: {skill_file_path}")
        print(f"[MEMORIA SQLite] Decisión: {decision} | Ecosistema: {target_eco or new_eco_name}")

    return prompt


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Uso: generate.py <role> <context> <task> [format] [--write] [skill_name]")
        print("Ejemplo: python generate.py 'Auditor de Calidad' 'Ecosistema de Software' 'Auditar cobertura de tests' 'xml' --write 'qa-tester'")
        sys.exit(1)

    role_arg = sys.argv[1]
    context_arg = sys.argv[2]
    task_arg = sys.argv[3]
    format_arg = sys.argv[4] if len(sys.argv) > 4 and not sys.argv[4].startswith('--') else "xml"
    
    do_write = "--write" in sys.argv
    skill_name_arg = None
    if "--write" in sys.argv:
        w_idx = sys.argv.index("--write")
        if w_idx + 1 < len(sys.argv):
            skill_name_arg = sys.argv[w_idx + 1]

    rendered_prompt = generate_crispe_skill(
        role=role_arg,
        context=context_arg,
        task=task_arg,
        format_str=format_arg,
        skill_name=skill_name_arg,
        write_file=do_write
    )

    if not do_write:
        print("\n--- PROMPT NEO-CRISPE v2.0 RENDERIZADO ---")
        print(rendered_prompt)
