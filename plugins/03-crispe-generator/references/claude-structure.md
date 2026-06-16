# Estructura Optimizada para Claude (Anthropic)

Basado en la "Estructura de un prompt para Claude", este documento define la jerarquía obligatoria para maximizar la comprensión de modelos basados en la arquitectura de Anthropic.

## 1. Uso Extensivo de Etiquetas XML
Claude fue entrenado exhaustivamente con XML. Todo prompt generado para ecosistemas que utilicen Claude debe seguir esta convención:
- `<role>`: Definición del agente.
- `<context>`: Datos de fondo y dominio.
- `<task>`: La instrucción principal.
- `<rules>` o `<constraints>`: Restricciones innegociables (ej. SOC 2).
- `<examples>`: Ejemplos de input/output.
- `<format>`: Estructura de salida deseada.

## 2. Prafaseo y "Prefilling"
- **Respuesta Prefabricada:** Iniciar la respuesta de Claude con un tag específico para forzar la estructura de salida. Ej: Si se pide un JSON, terminar el prompt con `{"response":` para evitar texto previo.

## 3. Manejo de Documentos Largos
- **Data First, Task Last:** Enviar los documentos extensos (código, PDFs) en etiquetas `<document>` al inicio del prompt, y la pregunta o tarea al final. Claude retiene mejor los detalles si la tarea sigue inmediatamente a la carga cognitiva de lectura.
