# Reglas Operativas y Estándares de Renderizado: img2threejs Ecosystem

**Propósito:** Definir los principios inmutables para la síntesis de modelos 3D procedurales en Three.js a partir de imágenes 2D mediante visión multimodal de **Gemini 3.8 Flash**, asegurando código TypeScript limpio, libre de mallas binarias externas (`.glb`/`.gltf`), optimizado para WebGL/WebGPU a 60–120 FPS.  
**Cumplimiento Normativo:** ISO 25010 (Eficiencia de Rendimiento y Mantenibilidad de Software), W3C WebGL 2.0 / WebGPU Standard, ISO/IEC 42001 (AIMS).

---

## 1. Principio Inmutable de Código Procedural Puro (Zero External Binary Blobs)

1. **Cero Dependencia de Archivos Binarios Externos:**
   - Queda estrictamente prohibido que el generador dependa de la carga de archivos `.glb`, `.obj` o `.fbx` alojados externamente.
   - Toda la geometría debe sintetizarse proceduralmente usando primitivas de Three.js (`BoxGeometry`, `CylinderGeometry`, `SphereGeometry`, `ConeGeometry`, `TorusGeometry`, `ExtrudeGeometry`, `LatheGeometry`) o `BufferGeometry` con atributos de posición y normales calculados algorítmicamente.
2. **Texturas y Materiales Procedurales:**
   - Evitar texturas PNG/JPEG externas que provoquen fallos de CORS o tiempos de carga lentos. Emplear texturas procedurales generadas en canvas HTML5 (`CanvasTexture`), sombreadores WGSL/GLSL o propiedades de materiales PBR nativos (`MeshStandardMaterial`, `MeshPhysicalMaterial`).

---

## 2. Protocolo de Inferencia de Visión Multimodal con Gemini 3.8 Flash

1. **Descomposición Volumétrica Guiada por Gemini 3.8 Flash:**
   - El análisis de imagen debe invocar el modelo `gemini-3.8-flash` con `thinking_level: high` utilizando el esquema estructurado `ObjectSculptSpec`.
   - La red debe identificar:
     * Jerarquía de partes (`root`, `chassis`, `subassemblies`, `pivots`).
     * Dimensiones relativas $[w, h, d]$ y posiciones relativas $[x, y, z]$.
     * Propiedades físicas PBR: `color`, `roughness`, `metalness`, `clearcoat`, `transmission` y `emissive`.
2. **Preservación de Ejes y Pivotes de Rotación:**
   - Cada articulación o componente móvil (ruedas, tapas, hélices, extremidades) debe anclarse a su propio `THREE.Group` con el punto de pivote corregido para permitir animación limpia.

---

## 3. Presupuesto de Rendimiento y Calidad de Código (ISO 25010)

1. **Límites de Geometría y Llamadas de Dibujo (*Draw Calls*):**
   - Presupuesto máximo por objeto: $<15.000$ triángulos y $<35$ draw calls.
   - En componentes estáticos repetitivos, emplear `InstancedMesh` o fusión de geometrías (`BufferGeometryUtils.mergeGeometries`).
2. **Ciclo de Vida y Limpieza de Memoria (*Disposal Pattern*):**
   - Toda fábrica de Three.js generada debe exportar un método de destrucción o registrar el desecho de recursos:
     ```typescript
     function disposeModel(model: THREE.Group): void {
       model.traverse((child) => {
         if ((child as THREE.Mesh).isMesh) {
           const mesh = child as THREE.Mesh;
           mesh.geometry.dispose();
           if (Array.isArray(mesh.material)) {
             mesh.material.forEach((m) => m.dispose());
           } else {
             mesh.material.dispose();
           }
         }
       });
     }
     ```
3. **Loop de Animación Integrado (`.update(delta)`):**
   - El grupo raíz devuelto debe implementar una función `.update(delta: number)` que anime componentes secundarios (rotaciones continuas, balanceo sutil, flotación o pulsos lumínicos).
