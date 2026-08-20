# Three.js Enterprise Architecture Mastery — WebGPU, TSL, BatchedMesh & Spatial BVH

**Referencia Oficial:** Three.js Core Architecture (`mrdoob/three.js`) — Versiones r160+  
**Objetivo:** Guía técnica maestra para la ingeniería de gráficos 3D Web de alto rendimiento, compilación multiplataforma WebGL2/WebGPU y optimización extrema de Draw Calls.  
**Cumplimiento Normativo:** ISO 25010 (Eficiencia de Recursos & Mantenibilidad), DORA (Garantía de 60+ FPS fijos).

---

## 1. El Nuevo Paradigma: WebGPURenderer & TSL (Three.js Shading Language)

### A. WebGPURenderer vs WebGLRenderer Clásico
A partir de las versiones recientes de Three.js, el motor introduce un pipeline unificado basado en **Nodos (Node Material System)** capaz de compilar automáticamente tanto a **WGSL** (WebGPU) como a **GLSL ES 3.0** (WebGL2):

```typescript
import * as THREE from 'three/webgpu';

// Inicialización de Renderer Híbrido (WebGPU con fallback automático a WebGL2)
const renderer = new THREE.WebGPURenderer({ antialias: true });
await renderer.init();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);
```

### B. TSL (Three.js Shading Language)
TSL reemplaza las cadenas de texto GLSL concatenadas manualmente por un grafo de funciones y nodos tipados en TypeScript/JavaScript, eliminando errores de sintaxis en tiempo de ejecución:

```typescript
import { 
  Fn, uv, texture, color, float, vec2, vec3, vec4, sin, time, mix, dot, cross, normalize,
  MeshStandardNodeMaterial 
} from 'three/tsl';

// Definición de una función TSL reutilizable
const waveDistortion = Fn(([baseUv, speed, frequency]) => {
  const animatedUv = baseUv.add(vec2(sin(time.mul(speed).add(baseUv.x.mul(frequency))), 0.0).mul(0.05));
  return animatedUv;
});

// Creación de Material Nodal
const material = new MeshStandardNodeMaterial();
const distortedUv = waveDistortion(uv(), float(2.0), float(10.0));

material.colorNode = mix(color(0x07283d), color(0xffd231), sin(time));
material.roughnessNode = float(0.2);
material.metalnessNode = float(0.8);
material.positionNode = positionLocal.add(vec3(0.0, sin(time.add(positionLocal.x.mul(5.0))).mul(0.2), 0.0));
```

---

## 2. Shaders de Cómputo (Compute Shaders) en GPU

Para simulaciones masivas (partículas, boids, campos de velocidad, transformaciones matriciales de 100,000+ elementos), WebGPU permite la ejecución en paralelo de **Compute Shaders** sin tocar la CPU:

```typescript
import { storage, Fn, instanceIndex, vec3, float } from 'three/tsl';

const particleCount = 100000;
const positionBuffer = new THREE.StorageBufferAttribute(new Float32Array(particleCount * 3), 3);
const positionStorage = storage(positionBuffer, 'vec3', particleCount);

// Compute Kernel
const computeParticles = Fn(() => {
  const index = instanceIndex;
  const currentPos = positionStorage.element(index);
  const newPos = currentPos.add(vec3(0.0, float(0.01), 0.0));
  positionStorage.element(index).assign(newPos);
})().compute(particleCount);

// En el bucle de render:
renderer.compute(computeParticles);
renderer.render(scene, camera);
```

---

## 3. Compresión Extrema de Draw Calls: `BatchedMesh` & `InstancedMesh`

### A. BatchedMesh (La Revolución de Dibujo Masivo)
`BatchedMesh` permite combinar múltiples mallas con **geometrías diferentes** y compartir un único material en **un solo Draw Call**, permitiendo modificar independientemente matrices de transformación, cajas de límites (Bounding Boxes) y visibilidad por instancia:

```typescript
const maxGeometryCount = 500;
const maxVertexCount = 100000;
const maxIndexCount = 150000;

const batchedMesh = new THREE.BatchedMesh(
  maxGeometryCount, 
  maxVertexCount, 
  maxIndexCount, 
  material
);

// Agregar geometrías al lote
const geomId1 = batchedMesh.addGeometry(boxGeometry);
const geomId2 = batchedMesh.addGeometry(sphereGeometry);

// Agregar instancias en el espacio
const instanceId1 = batchedMesh.addInstance(geomId1);
const instanceId2 = batchedMesh.addInstance(geomId2);

const matrix = new THREE.Matrix4();
matrix.setPosition(10, 0, 5);
batchedMesh.setMatrixAt(instanceId1, matrix);
```

### B. Matriz de Decisión de Rendimiento:
| Técnica | Geometrías | Materiales | Draw Calls | Caso de Uso |
| :--- | :--- | :--- | :--- | :--- |
| **Mallas Clásicas (`THREE.Mesh`)** | Diferentes | Diferentes | 1 por malla ($N$ calls) | Elementos hero / únicos |
| **`InstancedMesh`** | Idéntica | Idéntico | 1 Draw Call | Bosques, partículas, césped |
| **`BatchedMesh`** | Heterogéneas | Mismo Material | 1 Draw Call | Ciudades, interiores, props |

---

## 4. Aceleración Espacial con BVH (Bounding Volume Hierarchy)

El trazado de rayos tradicional de Three.js itera sobre cada triángulo ($O(N)$). Con **`three-mesh-bvh`**, el raycasting se acelera a $O(\log N)$, permitiendo consultas de colisión en tiempo real sobre millones de polígonos:

```typescript
import { computeBoundsTree, disposeBoundsTree, acceleratedRaycast } from 'three-mesh-bvh';

// Extender geometrías y mallas con BVH
THREE.BufferGeometry.prototype.computeBoundsTree = computeBoundsTree;
THREE.BufferGeometry.prototype.disposeBoundsTree = disposeBoundsTree;
THREE.Mesh.prototype.raycast = acceleratedRaycast;

const complexGeometry = new THREE.TorusKnotGeometry(10, 3, 300, 50);
complexGeometry.computeBoundsTree(); // Genera árbol jerárquico

const mesh = new THREE.Mesh(complexGeometry, material);
scene.add(mesh);

// Raycasting ultra-rápido a 60 FPS
const raycaster = new THREE.Raycaster();
raycaster.firstHitOnly = true; // Optimización de salida rápida
const hits = raycaster.intersectObject(mesh);
```

---

## 5. Pipeline de Post-Procesado y Tone Mapping de Grado Cinematográfico

```typescript
import { EffectComposer } from 'three/examples/jsm/postprocessing/EffectComposer.js';
import { RenderPass } from 'three/examples/jsm/postprocessing/RenderPass.js';
import { GTAOPass } from 'three/examples/jsm/postprocessing/GTAOPass.js';
import { UnrealBloomPass } from 'three/examples/jsm/postprocessing/UnrealBloomPass.js';
import { OutputPass } from 'three/examples/jsm/postprocessing/OutputPass.js';

renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 1.1;

const composer = new EffectComposer(renderer);
composer.addPass(new RenderPass(scene, camera));

// Oclusión Ambiental de Ground Truth (GTAO)
const gtaoPass = new GTAOPass(scene, camera, window.innerWidth, window.innerHeight);
gtaoPass.output = GTAOPass.OUTPUT.Default;
composer.addPass(gtaoPass);

// Bloom Físico Selectivo
const bloomPass = new UnrealBloomPass(new THREE.Vector2(window.innerWidth, window.innerHeight), 0.35, 0.4, 0.85);
composer.addPass(bloomPass);

composer.addPass(new OutputPass());
```

---

## 6. Deformación de Mallas en VRAM con WebGPU Compute Shaders (Zero-GC)

Integrando las técnicas del [`webgl-sculpt-geometry-ecosystem`](file:///c:/Users/Nomack/Documents/workspace/agents/antigravity/dev/prompt-generator/agents-factory/webgl-sculpt-geometry-ecosystem), WebGPU permite la deformación interactiva de vértices directamente en la memoria VRAM sin pasar por la CPU ni generar pausas de recolección de basura (*Zero Garbage Collection*):

```typescript
import * as THREE from 'three/webgpu';
import { Fn, storage, instanceIndex, vec3, float, clamp } from 'three/tsl';

// Buffer de almacenamiento para deformación continua en GPU
const positionBuffer = new THREE.StorageBufferAttribute(geometry.attributes.position.array as Float32Array, 3);
const positionStorage = storage(positionBuffer, 'vec3', geometry.attributes.position.count);

export function createMeshDeformComputeNode(brushCenter: THREE.Vector3, brushNormal: THREE.Vector3, radius: number, intensity: number) {
  const centerNode = vec3(brushCenter.x, brushCenter.y, brushCenter.z);
  const normalNode = vec3(brushNormal.x, brushNormal.y, brushNormal.z);
  const radiusNode = float(radius);
  const intensityNode = float(intensity);

  return Fn(() => {
    const idx = instanceIndex;
    const currentPos = positionStorage.element(idx);
    const dist = currentPos.distance(centerNode);

    // Hermite Falloff: (1 - (d/r)^2)^3
    const normDist = clamp(dist.div(radiusNode), float(0.0), float(1.0));
    const falloff = float(1.0).sub(normDist.mul(normDist)).pow(float(3.0));
    const newPos = currentPos.add(normalNode.mul(falloff).mul(intensityNode));

    positionStorage.element(idx).assign(newPos);
  })().compute(geometry.attributes.position.count);
}
```

