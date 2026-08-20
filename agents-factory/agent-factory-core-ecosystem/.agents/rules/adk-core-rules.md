# Reglas Operacionales de Meta-Orquestación y Gestión de Agentes (Google ADK)

**Alcance:** Creación, configuración, evaluación y ejecución de sistemas multi-agente en Antigravity  
**Normativa:** ISO 42001 (AIMS), ISO 25010 (Fiabilidad y Calidad de Software), DORA.

---

## 1. Principio de No Invasión y Acoplamiento Limpio

1. **Preservación de Ecosistemas Existentes:**
   - La introducción de workflows de ADK no debe romper contratos existentes, nombres de carpetas ni dependencias funcionales de otros ecosistemas. Debe actuar como una capa de optimización y aceleración.
2. **Modularidad Estricta:**
   - Cada agente definido mediante ADK debe tener responsabilidades únicas, descripciones semánticas claras (`description`) y esquemas de entrada/salida tipados.

---

## 2. Reglas de Ejecución y Límites de Recursión

1. **Límites de Bucles (`LoopAgent` / Evaluator-Optimizer):**
   - Todo bucle de refinamiento debe tener un parámetro `max_iterations` estricto (máximo 5 iteraciones por defecto) para prevenir llamadas infinitas y consumo desmedido de tokens.
2. **Criterios de Parada Explícitos:**
   - Los bucles deben evaluar una condición booleana de convergencia basada en una puntuación de corte (ej. score $\ge 0.85$ o cumplimiento del 100% de la rúbrica).

---

## 3. Reglas de Herramientas y Contratos de Datos

1. **Tipado Obligatorio:**
   - Todas las funciones y herramientas de agente deben declarar esquemas JSON Schema o modelos Pydantic con tipos primitivos, descripciones de parámetros y campos obligatorios explícitos.
2. **Manejo Seguro de Excepciones:**
   - Las herramientas nunca deben lanzar excepciones no capturadas al modelo. Deben atrapar errores y devolver mensajes de diagnóstico estructurados para permitir que el agente intente una estrategia de autocorrección.
