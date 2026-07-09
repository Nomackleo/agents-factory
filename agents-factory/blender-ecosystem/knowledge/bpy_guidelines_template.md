# Plantilla de Conocimiento: Blender Python API (`bpy`)

**Propósito (WHY):** Servir como *Ground Truth* para los agentes constructores (`topology-agent`, `lighting-agent`, etc.) al generar scripts de Blender, evitando alucinaciones de la API.

**Audiencia (WHO):** Agentes *Builders* y Orquestadores de VFX.

## Estructura Exegética Obligatoria (WHAT)

Todo script `bpy` generado por este ecosistema debe ser determinista, seguro (sin accesos a red o disco fuera del sandbox), y manejar sus propios contextos.

### 1. Inicialización y Limpieza de Escena
Los agentes no asumen un estado limpio de la escena. Siempre deben purgar datos previos (Mantenibilidad).

```python
import bpy

def clear_scene():
    """Elimina mallas, luces y cámaras existentes para garantizar determinismo."""
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()
    
    # Purgar datos huérfanos (Optimización de Memoria)
    for block in bpy.data.meshes:
        if block.users == 0:
            bpy.data.meshes.remove(block)
```

### 2. Operaciones Matemáticas y Topología
Evitar el uso de `bpy.ops` (lentos) cuando sea posible acceder directamente a `bpy.data` o usar `bmesh` para manipulación geométrica masiva (Eficiencia de Desempeño).

```python
import bmesh

def create_procedural_mesh():
    mesh = bpy.data.meshes.new("ProceduralMesh")
    obj = bpy.data.objects.new("ProceduralMeshObj", mesh)
    bpy.context.collection.objects.link(obj)
    
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=2.0)
    bm.to_mesh(mesh)
    bm.free()
```

## Prevención de Ruido (Heurística)
- **Creatividad:** Los agentes no deben adivinar nombres de materiales o nodos. Deben buscar la referencia exacta o instanciarlos por defecto.
- **Registro (Logging):** Imprimir por consola estados de éxito (`print("INFO: Lighting rig completed.")`) para que el Supervisor capte el flujo estándar sin analizar el código binario del archivo `.blend`.
