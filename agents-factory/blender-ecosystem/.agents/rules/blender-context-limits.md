# Políticas de Límite de Contexto para LLMs en Blender

Blender puede manejar escenas con millones de polígonos y miles de nodos. Extraer este estado vía MCP puede causar un desbordamiento de la ventana de contexto del LLM (Token Limit Exceeded). 

Para evitar esto, los agentes deben seguir estas restricciones al consultar información de la escena:

1. **NUNCA CONSULTAR ARRAYS DE VÉRTICES COMPLETOS:**
   En lugar de pedir la posición de cada vértice en un objeto, pide:
   - Número total de vértices/caras.
   - Bounding Box (Dimensiones X, Y, Z).
   - Centro de masa.

2. **ÁRBOLES DE NODOS COMPLEJOS:**
   No pidas que el MCP imprima todo el árbol de Geometry Nodes o Shader Nodes si tiene más de 15 nodos. En su lugar:
   - Pide los Nodos de Entrada (Inputs/Group Inputs) y sus valores actuales.
   - Pide los Nodos de Salida (Outputs).
   - Realiza búsquedas específicas (ej. "¿Existe un nodo llamado 'ColorRamp' y cuáles son sus paradas?").

3. **RESÚMENES SOBRE DATOS CRUDOS:**
   Si se requiere validar errores, no pidas todo el `Info Log`. Pide únicamente los últimos 5 errores lanzados por el intérprete de Python o el logger de Blender.
