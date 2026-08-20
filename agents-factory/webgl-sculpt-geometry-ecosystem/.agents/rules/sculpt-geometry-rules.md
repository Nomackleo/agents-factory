# Reglas Operacionales del Ecosistema WebGL/WebGPU Sculpt & Geometry

**Alcance:** Manipulación Geométrica, Escultura Digital 3D, Remallado y Topología Dinámica  
**Normativa:** ISO 25010 (Eficiencia de Recursos & Estabilidad de Memoria), DORA.

---

## 1. Reglas de Invarianza de Memoria (Zero-GC)

1. **Estructuras Planas Contiguas:**
   - La geometría activa debe residir exclusivamente en `Float32Array` y `Uint32Array`. Prohibida la creación de objetos temporales `new THREE.Vector3()` o arrays anidados dentro del bucle de trazo continuo del pincel (*onPointerMove*).
2. **Reutilización de Buffers (*Object Pooling*):**
   - Los vectores de cálculo de normales, tangentes y centroides deben ser pre-alocados como variables de módulo reutilizables.

---

## 2. Invarianza Topológica (2-Manifold)

1. **Garantía de Variedad Cerrada:**
   - Todo algoritmo de remallado volumétrico debe garantizar superficies estancas (*2-manifold watertight*) sin caras degeneradas (área cero), vértices duplicados o aristas compartidas por más de 2 triángulos.
2. **Preservación de Normales:**
   - Toda deformación de vértices debe recalcular las normales de superficie inmediatamente en el área afectada para evitar artefactos de iluminación en el sombreador PBR/MatCap.

---

## 3. Streaming Eficiente a GPU

1. **Evitar Re-uploads Totales:**
   - En WebGL clásico, usar siempre `gl.bufferSubData()` acotado al *bounding box* o rango de vértices modificados.
   - En WebGPU, ejecutar la deformación directamente en la GPU mediante Compute Shaders sobre `StorageBufferAttribute`.
