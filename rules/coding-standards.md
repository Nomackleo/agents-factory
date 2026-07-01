# Coding Standards y Determinismo Estructural

Las reglas para el código, configuraciones y prompts escritos por la fábrica.

## 1. Output Determinista
- **Uso Estricto de XML o JSON:** Las transiciones de estado entre agentes (handoffs) deben comunicarse usando exclusivamente estructuras delimitadas de forma rígida, como `<architect_blueprint>...</architect_blueprint>` o JSON puro con schema.
- **Sin Artefactos Literarios:** Evitar frases como "Aquí tienes la respuesta:" o "Espero que esto te sirva". Solo el output técnico puro para facilitar el parsing por hooks o regex.

## 2. Prompts como Código de Producción
- **Framework CRISPE:** Todo agente generado debe tener su `SKILL.md` basado en CRISPE (Capacity, Role, Instruction, Schema, Personality, Examples). No hay excepciones.
- **Few-Shot Examples:** Todo `SKILL.md` debe incluir al menos un caso de uso (Example) para anclar el comportamiento del LLM.

## 3. Estructuración y Modularidad
- Los ecosistemas generados deben evitar scripts monolíticos. Si un workflow supera los 5000 tokens, debe dividirse en subagentes o múltiples herramientas.
- Archivos YAML, JSON y Markdown deben adherirse a los estándares universales de espaciado e indentación (ej. 2 espacios para YAML).
