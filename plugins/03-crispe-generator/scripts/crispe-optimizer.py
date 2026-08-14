#!/usr/bin/env python3
"""
CRISPE Prompt Optimizer & Evaluator

Este script automatiza el diseño, optimización, A/B testing y validación de prompts
siguiendo el framework CRISPE y las directrices avanzadas de Google y Anthropic.
"""

import sys
import os
import json
import time
import re
from typing import List, Dict, Any, Tuple
from dataclasses import dataclass, asdict

# Códigos ANSI para dar estilo y color a la terminal
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"


@dataclass
class CrispePrompt:
    capacity: str = ""
    receipt: str = ""
    instruction: str = ""
    schema: str = ""
    personality: str = ""
    examples: str = ""

    def render(self, variables: Dict[str, Any] = None) -> str:
        """Renderiza el prompt formateado con todos los componentes del framework CRISPE."""
        parts = []
        if self.capacity:
            parts.append(f"{BOLD}[CAPACITY & ROLE]{RESET}\n{self.capacity}")
        if self.receipt:
            parts.append(f"{BOLD}[RECEIPT / CONTEXT]{RESET}\n{self.receipt}")
        if self.instruction:
            parts.append(f"{BOLD}[INSTRUCTION]{RESET}\n{self.instruction}")
        if self.schema:
            parts.append(f"{BOLD}[SCHEMA / STRUCTURE]{RESET}\n{self.schema}")
        if self.personality:
            parts.append(f"{BOLD}[PERSONALITY & STYLE]{RESET}\n{self.personality}")
        if self.examples:
            parts.append(f"{BOLD}[EXAMPLES]{RESET}\n{self.examples}")
        
        raw_prompt = "\n\n".join(parts)
        
        # Reemplazar variables si se proporcionan
        if variables:
            for k, v in variables.items():
                raw_prompt = raw_prompt.replace(f"{{{k}}}", str(v))
                raw_prompt = raw_prompt.replace(f"{{{{{k}}}}}", str(v))
        return raw_prompt


class JsonRepair:
    """Implementación de un analizador y reparador de JSON rotos o truncados."""

    @staticmethod
    def repair(broken_json: str) -> Tuple[Dict[str, Any], bool]:
        """
        Intenta limpiar y reparar una cadena de texto JSON rota o truncada.
        Devuelve el objeto parseado y un booleano indicando si requirió reparación.
        """
        # Eliminar bloques de código markdown
        clean_str = broken_json.strip()
        if clean_str.startswith("```"):
            lines = clean_str.split("\n")
            if lines[0].startswith("```"):
                lines = lines[1:]
            if lines and lines[-1].strip() == "```":
                lines = lines[:-1]
            clean_str = "\n".join(lines).strip()
        
        # Buscar el inicio y final del JSON
        start_idx = clean_str.find("{")
        if start_idx == -1:
            start_idx = clean_str.find("[")
            
        if start_idx == -1:
            return {}, False

        clean_str = clean_str[start_idx:]
        
        # Intentar parsear directamente
        try:
            return json.loads(clean_str), False
        except json.JSONDecodeError:
            pass

        # Iniciar lógica de reparación manual
        repaired_str = clean_str
        was_repaired = True

        # 1. Asegurar comillas en llaves/valores truncados al final
        # Si termina en medio de una palabra o clave
        if repaired_str[-1] not in ('}', ']', '"', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'true', 'false', 'null'):
            # Buscar si hay una comilla abierta previamente en la última línea
            last_line = repaired_str.split('\n')[-1]
            if last_line.count('"') % 2 != 0:
                repaired_str += '"'

        # 2. Eliminar comas finales que causan errores de parseo
        repaired_str = re.sub(r',\s*([}\]])', r'\1', repaired_str)
        
        # 3. Equilibrar llaves y corchetes
        open_brackets = []
        in_string = False
        escape = False

        for i, char in enumerate(repaired_str):
            if escape:
                escape = False
                continue
            if char == '\\':
                escape = True
                continue
            if char == '"':
                in_string = not in_string
                continue
            
            if not in_string:
                if char in ('{', '['):
                    open_brackets.append(char)
                elif char in ('}', ']'):
                    if open_brackets:
                        last_open = open_brackets[-1]
                        if (char == '}' and last_open == '{') or (char == ']' and last_open == '['):
                            open_brackets.pop()

        # Cerrar en orden inverso
        while open_brackets:
            last_open = open_brackets.pop()
            if last_open == '{':
                repaired_str += '}'
            elif last_open == '[':
                repaired_str += ']'

        # Intentar parsear el JSON reparado
        try:
            return json.loads(repaired_str), True
        except json.JSONDecodeError as e:
            # Fallback secundario si sigue fallando: extraer pares clave-valor simples con regex
            fallback_dict = {}
            pairs = re.findall(r'"([^"]+)"\s*:\s*(?:"([^"]*)"|(\d+)|(true|false|null))', repaired_str)
            for pair in pairs:
                key = pair[0]
                val = pair[1] if pair[1] else (int(pair[2]) if pair[2] else (pair[3] == 'true' if pair[3] in ('true','false') else None))
                fallback_dict[key] = val
            if fallback_dict:
                return fallback_dict, True
            raise e


class MockLLMClient:
    """Simulador de LLM para pruebas unitarias y demostraciones interactiva."""
    
    def complete(self, prompt: str) -> str:
        # Simula respuestas según el tipo de tarea
        if "[CAPACITY & ROLE]" in prompt:
            # Si tiene estructura CRISPE
            if "sentiment" in prompt.lower() or "opinión" in prompt.lower():
                return '{\n  "sentiment": "POSITIVO",\n  "confidence": 0.95\n}'
            elif "código" in prompt.lower() or "code" in prompt.lower():
                return '```python\ndef saludo():\n    print("Hola Mundo")\n```'
            else:
                return "Respuesta simulada optimizada bajo el rol solicitado."
        else:
            # Prompt informal
            return "Respuesta genérica del modelo para prompt sin estructura."


class PromptABTester:
    """Clase encargada de ejecutar pruebas comparativas (A/B testing) entre variaciones."""

    def __init__(self, llm_client):
        self.client = llm_client

    def run_ab_test(self, prompt_a: str, prompt_b: str, test_inputs: List[Dict[str, Any]], expected_outputs: List[str]) -> Dict[str, Any]:
        results_a = []
        results_b = []
        latencies_a = []
        latencies_b = []

        print(f"\n{YELLOW}Iniciando A/B Test...{RESET}")
        
        for idx, (inp, exp) in enumerate(zip(test_inputs, expected_outputs)):
            # Test A
            start = time.time()
            render_a = prompt_a.format(**inp) if "{" in prompt_a else prompt_a
            resp_a = self.client.complete(render_a)
            latencies_a.append(time.time() - start)
            acc_a = 1.0 if resp_a.strip().lower() == exp.strip().lower() or exp.strip().lower() in resp_a.strip().lower() else 0.0
            results_a.append(acc_a)

            # Test B
            start = time.time()
            render_b = prompt_b.format(**inp) if "{" in prompt_b else prompt_b
            resp_b = self.client.complete(render_b)
            latencies_b.append(time.time() - start)
            acc_b = 1.0 if resp_b.strip().lower() == exp.strip().lower() or exp.strip().lower() in resp_b.strip().lower() else 0.0
            results_b.append(acc_b)

        avg_acc_a = sum(results_a) / len(results_a)
        avg_acc_b = sum(results_b) / len(results_b)
        avg_lat_a = sum(latencies_a) / len(latencies_a)
        avg_lat_b = sum(latencies_b) / len(latencies_b)

        winner = "B" if avg_acc_b >= avg_acc_a else "A"
        
        return {
            "prompt_a": {
                "avg_accuracy": avg_acc_a,
                "avg_latency_sec": avg_lat_a
            },
            "prompt_b": {
                "avg_accuracy": avg_acc_b,
                "avg_latency_sec": avg_lat_b
            },
            "winner": winner,
            "improvement_pct": abs(avg_acc_b - avg_acc_a) * 100
        }


def generate_crispe_from_informal(informal_prompt: str) -> CrispePrompt:
    """Conversor inteligente (heurística) para reestructurar prompts informales a CRISPE."""
    crispe = CrispePrompt()
    crispe.instruction = informal_prompt
    
    # Intentar extraer rol
    if "como" in informal_prompt.lower():
        match = re.search(r'(?:actúa como|se un|como un)\s+([^,.]+)', informal_prompt, re.IGNORECASE)
        if match:
            crispe.capacity = f"Actúa como un {match.group(1).strip()}."
            # Limpiar la instrucción del rol redundante
            crispe.instruction = informal_prompt.replace(match.group(0), "").strip()

    # Si no se detectó rol, asignar uno genérico relevante
    if not crispe.capacity:
        crispe.capacity = "Actúa como un asistente virtual experto y analista de sistemas."

    # Intentar extraer formato
    if "json" in informal_prompt.lower():
        crispe.schema = "Devuelve el resultado estructurado en formato JSON válido."
    elif "tabla" in informal_prompt.lower():
        crispe.schema = "Estructura la información en una tabla de Markdown clara."
    else:
        crispe.schema = "Devuelve una respuesta estructurada con títulos y viñetas claros."

    # Añadir personalidad estándar
    crispe.personality = "Tono profesional, conciso y directo al grano. Evita preámbulos conversacionales."

    return crispe


def run_unit_tests():
    """Ejecuta las pruebas unitarias integradas del optimizador y validador."""
    print(f"{BOLD}Ejecutando pruebas de validacion interna...{RESET}")
    
    # 1. Test CRISPE Rendering
    prompt = CrispePrompt(
        capacity="Actua como programador.",
        instruction="Escribe un hello world.",
        schema="Formato de script."
    )
    rendered = prompt.render()
    assert "[CAPACITY & ROLE]" in rendered, "Fallo render de Capacity"
    assert "[INSTRUCTION]" in rendered, "Fallo render de Instruction"
    assert "[SCHEMA / STRUCTURE]" in rendered, "Fallo render de Schema"
    print(f"{GREEN}[OK] Test CRISPE Rendering exitoso.{RESET}")

    # 2. Test JSON Repair
    broken_json = '{"nombre": "Cliente", "deuda": 500,'
    repaired, status = JsonRepair.repair(broken_json)
    assert status == True, "Deberia haber sido reparado"
    assert repaired["nombre"] == "Cliente", "Clave 'nombre' no coincide"
    assert repaired["deuda"] == 500, "Clave 'deuda' no coincide"
    
    broken_json_2 = '```json\n{"status": "ok", "tags": ["ia", "prompts"]\n```'
    repaired_2, status_2 = JsonRepair.repair(broken_json_2)
    assert repaired_2["status"] == "ok", "Falla remocion de bloques de codigo markdown"
    assert "prompts" in repaired_2["tags"], "Falla balanceo de corchetes"
    print(f"{GREEN}[OK] Test JSON Repair exitoso.{RESET}")

    # 3. Test A/B Testing & Conversor
    tester = PromptABTester(MockLLMClient())
    informal = "Clasifica si este correo es importante o no"
    crispe = generate_crispe_from_informal(informal)
    
    inputs = [{"text": "Urgente, revisar pago."}]
    exp = ["POSITIVO"] # mock output del simulador
    
    res = tester.run_ab_test(informal, crispe.render(), inputs, exp)
    assert "winner" in res, "Deberia retornar un ganador del test"
    print(f"{GREEN}[OK] Test A/B Testing & Conversor exitoso.{RESET}")

    # 4. Test Semantic Memory Lookup (Codebase-Memory-MCP SQLite)
    from semantic_memory_lookup import lookup_memory
    mem_res = lookup_memory("auditoría de seguridad web")
    assert "decision" in mem_res, "Fallo consulta a memoria SQLite"
    assert mem_res["decision"] in ("ATTACH_SKILL", "CREATE_ECOSYSTEM"), "Decisión de memoria invalida"
    print(f"{GREEN}[OK] Test Búsqueda en Memoria Persistente SQLite exitoso.{RESET}")
    print(f"\n{GREEN}{BOLD}Todas las comprobaciones pasaron correctamente.{RESET}")


def interactive_mode():
    """Modo interactivo en terminal para que el usuario diseñe y optimice su prompt."""
    print(f"\n{BLUE}{BOLD}=== CREADOR INTERACTIVO DE PROMPTS CRISPE ==={RESET}")
    print("Introduce los detalles de tu prompt informal o presiona Enter para usar datos de prueba:")
    
    informal = input(f"\n{BOLD}Tu prompt informal:{RESET} ").strip()
    if not informal:
        informal = "Quiero analizar las ventas mensuales y obtener ideas de mejora"
        print(f"Usando prompt por defecto: '{informal}'")
        
    crispe = generate_crispe_from_informal(informal)
    
    print(f"\n{GREEN}Prompt generado con CRISPE:{RESET}")
    print("-" * 60)
    print(crispe.render())
    print("-" * 60)

    # Permitir modificar campos interactivos
    while True:
        print(f"\n{BOLD}¿Deseas afinar algún componente?{RESET}")
        print("1. Modificar Rol (Capacity & Role)")
        print("2. Modificar Instrucción")
        print("3. Modificar Esquema de Salida (Schema)")
        print("4. Guardar y Salir")
        
        opt = input("Elige una opción (1-4): ").strip()
        if opt == "1":
            crispe.capacity = input("Nuevo Rol: ").strip()
        elif opt == "2":
            crispe.instruction = input("Nueva Instrucción: ").strip()
        elif opt == "3":
            crispe.schema = input("Nuevo Esquema: ").strip()
        elif opt == "4":
            break
            
    final_prompt = crispe.render()
    print(f"\n{GREEN}{BOLD}Prompt Final Guardado:{RESET}")
    print(final_prompt)


def main():
    if len(sys.argv) > 1:
        if "--test" in sys.argv:
            run_unit_tests()
            sys.exit(0)
        elif "--interactive" in sys.argv:
            interactive_mode()
            sys.exit(0)
        elif "--prompt" in sys.argv:
            prompt_idx = sys.argv.index("--prompt")
            if prompt_idx + 1 < len(sys.argv):
                user_p = sys.argv[prompt_idx + 1]
                crispe = generate_crispe_from_informal(user_p)
                print(f"\n{GREEN}{BOLD}Prompt Convertido a CRISPE:{RESET}")
                print(crispe.render())
                
                if "--run-tests" in sys.argv:
                    tester = PromptABTester(MockLLMClient())
                    inputs = [{"text": "Ejemplo"}]
                    exp = ["POSITIVO"]
                    res = tester.run_ab_test(user_p, crispe.render(), inputs, exp)
                    print(json.dumps(res, indent=2))
                sys.exit(0)
                
    # Ayuda básica si no hay argumentos válidos
    print("CRISPE Prompt Optimizer CLI")
    print("Opciones:")
    print("  --test          : Ejecuta los tests unitarios automatizados del script.")
    print("  --interactive   : Lanza el creador y optimizador de prompts interactivo.")
    print("  --prompt <txt>  : Convierte un prompt informal al framework CRISPE.")
    print("  --run-tests     : Corre simulación de A/B test sobre el prompt convertido.")


if __name__ == '__main__':
    main()
