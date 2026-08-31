# CADAM WebAssembly & Web Worker Architecture: High-Performance In-Browser CAD

**Propósito:** Especificación de la arquitectura de compilación de OpenSCAD en WebAssembly (WASM), comunicación asíncrona mediante Web Workers y pipeline de exportación a Three.js / STL / 3MF.  
**Cumplimiento Normativo:** ISO 25010 (Eficiencia de Desempeño y Capacidad de Respuesta), W3C WebAssembly Standard.

---

## 1. Topología del Pipeline de Compilación

Para mantener una experiencia de usuario fluida a 60–120 FPS sin bloquear el hilo principal de renderizado de la interfaz:

```mermaid
graph LR
    subgraph MainThread["Hilo Principal (React / TanStack / Three.js)"]
        UI[Sliders Paramétricos / Input Prompt] -->|PostMessage: parameters| WW[Web Worker Manager]
        T3D[Three.js Viewport] <--|Transferable ArrayBuffer: vertices/indices| WW
    end

    subgraph WebWorker["Web Worker (Background Thread)"]
        WW --> SCADEngine["OpenSCAD WASM Runtime"]
        SCADEngine --> CSGEval["Evaluación CSG (Clipper / CGAL)"]
        CSGEval --> MeshGen["Generación de Malla / STL Parser"]
        MeshGen --> BufferPrep["BufferGeometry Serializer"]
    end
```

---

## 2. Protocolo de Mensajería del Web Worker

### Mensaje de Entrada (Main ➔ Worker):
```json
{
  "type": "COMPILE_SCAD",
  "payload": {
    "code": "difference() { cube([50,50,20]); cylinder(r=10, h=30); }",
    "params": {
      "box_width": 50,
      "hole_radius": 10
    },
    "export_format": "stl_buffer"
  }
}
```

### Mensaje de Respuesta (Worker ➔ Main con Objetos Transferibles):
```javascript
// En el Web Worker
const vertices = new Float32Array(geometryData.vertices);
const normals = new Float32Array(geometryData.normals);

self.postMessage({
  type: "COMPILE_SUCCESS",
  payload: {
    vertices,
    normals,
    trianglesCount: vertices.length / 9
  }
}, [vertices.buffer, normals.buffer]); // Transferencia O(1) de memoria sin clonado
```

---

## 3. Exportadores de Archivos Soportados

1. **`STL` (Stereolithography):** Formato universal para impresión 3D (binario y ASCII).
2. **`3MF` (3D Manufacturing Format):** Formato XML comprimido moderno con metadatos de color, material y unidades precisas en milímetros.
3. **`STEP` (Standard for the Exchange of Product model data):** Formato B-Rep de ingeniería para importar en SolidWorks, Fusion 360, FreeCAD e Inventor.
4. **`GLTF / GLB`:** Formato web optimizado para visualización en Three.js, Babylon.js y WebGPU.
5. **`SCAD`:** Código fuente paramétrico original para archivo soberano.
