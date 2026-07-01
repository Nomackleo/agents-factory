# Bucle de Evaluación y Corrección (Evaluation Loop)

Este es el diagrama de flujo que el **Supervisor (00)** y los **Builders (03)** deben seguir para asegurar que los comandos enviados a Blender logran el objetivo propuesto por el usuario.

## Fases del Bucle

### 1. Inyección y Ejecución
El `Builder` especializado (ej. `topology-agent`) escribe un script en Python y se lo pasa al `Supervisor`.
El `Supervisor` valida el script contra las reglas de seguridad (`mcp-security-policy.md`) y lo envía a Blender mediante la herramienta MCP de Anthropic.

### 2. Extracción de Estado (State Extraction)
Inmediatamente después de la ejecución, el `Supervisor` realiza una consulta de estado (State Check). Dependiendo de la tarea, consulta:
- **Errores de Sintaxis:** ¿El comando devolvió un `Traceback (most recent call last)`?
- **Validación Topológica:** Usando un script corto, verifica si el objeto tiene caras no-manifold (si aplica).
- **Validación Visual/Estructural:** Extrae la Bounding Box, cantidad de vértices, y lista de materiales del objeto modificado para ver si coinciden con lo esperado.

### 3. Evaluación (Evaluation)
El `Supervisor` compara el "Estado Actual" contra el "Estado Deseado".
- **Caso A (Éxito):** El estado coincide. El supervisor le informa al usuario o continúa con la siguiente etapa del flujo arquitectónico.
- **Caso B (Fallo):** El estado no coincide o hubo un error de código.

### 4. Iteración y Corrección (Iteration)
Si ocurre el Caso B, el `Supervisor` NO se rinde. 
Envía un mensaje de vuelta al `Builder` que ejecutó el código original con el siguiente payload:
`[ERROR TRACE / CONTEXT] + [INSTRUCCIÓN DE CORRECCIÓN]`
El `Builder` debe re-escribir el código, evitando el error previo, y devolverlo al Supervisor.

**Límite:** Se permiten un máximo de 3 iteraciones por nodo. Si falla la 3ra vez, el Supervisor hace un *Handoff* al usuario para intervención manual.
