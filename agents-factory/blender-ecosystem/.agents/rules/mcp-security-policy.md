# Políticas de Seguridad MCP (Blender Ecosystem)

Dado que `blender-mcp` ejecuta código Python directamente en la máquina del host a través del socket de Blender sin un sandbox nativo, todos los agentes deben adherirse estrictamente a las siguientes reglas:

1. **PROHIBIDO EL USO DE MÓDULOS DE SISTEMA DESTRUCTIVOS:**
   Bajo NINGUNA circunstancia los agentes generarán código Python que importe o utilice módulos para interactuar con el sistema operativo fuera del directorio del proyecto (`bpy.path.abspath('//')`).
   - Bloqueado: `os.system`, `os.remove`, `shutil.rmtree`, `subprocess.call` (a menos que sea explícitamente para llamar binarios empaquetados autorizados).
   
2. **NO EJECUCIÓN DE CÓDIGO EXTERNO:**
   No descargar y ejecutar scripts usando `requests`, `urllib` o `eval()`/`exec()`. Todo código debe ser explícitamente escrito en la consola de Blender.

3. **PROTECCIÓN DE ARCHIVOS DEL USUARIO:**
   Nunca sobreescribir el archivo actual (`bpy.ops.wm.save_mainfile()`) sin confirmación explícita. Trabajar siempre sobre copias, prefiriendo usar `bpy.ops.wm.save_as_mainfile()` con sufijos `_agent_vX`.

4. **VALIDACIÓN PRE-INYECCIÓN:**
   El Supervisor (`00-supervisor-router`) debe inspeccionar el payload de Python generado por los `builders` antes de enviarlo al servidor MCP. Si detecta importaciones prohibidas, debe rechazar el payload y penalizar la ejecución en el bucle iterativo.
