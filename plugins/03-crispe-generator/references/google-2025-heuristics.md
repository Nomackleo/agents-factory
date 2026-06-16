# Heurísticas de Alto Rendimiento: Google 2025

Este documento condensa los principios del "Prompt Engineering by Google 2025" para garantizar la economía de tokens (Token Economy) y la máxima precisión (Zero Hallucination).

## 1. Economía de Tokens (Token Economy)
- **Eliminar Verbosidad:** Omitir fórmulas de cortesía ("por favor", "gracias", "actúa como un experto"). Ir directo a la asignación del rol y la tarea.
- **Formato Markdown Estricto:** Usar listas y viñetas en lugar de párrafos narrativos. El LLM procesa estructuras jerárquicas con menor costo de atención computacional.
- **Restricción de Output:** Definir el formato de salida explícitamente (ej. `Output MUST BE a valid JSON without markdown wrapping`).

## 2. Inyección de Contexto Dinámico
- **Context Window Management:** Poner el contexto de negocio al principio y las instrucciones ejecutables al final. El modelo pondera con mayor fuerza los tokens finales (Recency Bias).
- **Separadores Delimitados:** Usar delimitadores claros como `###`, `---`, o tags XML `<section>` para separar instrucciones de datos de usuario.

## 3. Heurísticas Cognitivas
- **Chain of Thought (CoT) Dirigido:** Forzar al modelo a pensar en un bloque separado antes de dar la respuesta final. Ej: `<thought_process>...</thought_process>`.
- **Ejemplos Few-Shot:** Proveer 1 o 2 ejemplos positivos y 1 negativo (Edge Case) reduce la desviación estándar de la respuesta en un 40%.
