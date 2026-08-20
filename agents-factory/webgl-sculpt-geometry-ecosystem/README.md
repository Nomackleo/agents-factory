# WebGL / WebGPU Sculpt & Geometry Ecosystem — Universal Antigravity Architecture

**Autoría Oficial:** Leonel Salcedo (Nomack Studio)  
**WHAT**: Ecosistema Agéntico Dedicado para la Escultura Digital 3D en la Web, Algoritmos de Deformación Malla en Tiempo Real, Topología Dinámica (Dyntopo), Remallado Volumétrico (Manifold Dual Contouring / SurfaceNets), Aceleración Espacial (Octrees / SAH BVH) y Compute Shaders en GPU inspirados en el estado del arte de **SculptGL & Nomad Sculpt**.  
**Cumplimiento Normativo:** ISO 9001:2015, ISO 42001 (AIMS), ISO 27001 (ISMS), NIST CSF 2.0, DORA & `implicit/`.

---

## 1. Misión y Alcance del Ecosistema

El **WebGL / WebGPU Sculpt & Geometry Ecosystem** encapsula los algoritmos y pipelines matemáticos necesarios para manipular geometría tridimensional en tiempo real en el navegador:

1. **Escultura Digital Interactiva:** Pinceles deformadores (Clay, Smooth, Flatten, Pinch, Crease, Move, Inflate, Twist) con curvas de caída suaves y cálculo de distancia geodésica.
2. **Topología Dinámica (Dyntopo):** Subdivisión y colapso de aristas local en tiempo real sin congelamiento del hilo principal.
3. **Remallado Volumétrico & Reparación de Mallas:** Conversión de nubes de puntos y volúmenes SDF en mallas estancas cerradas (*watertight*) mediante **Manifold Dual Contouring**.
4. **Aceleración Espacial y Streaming a GPU:** Índices espaciales BVH y Octree para picking $O(\log N)$, y Compute Shaders en WebGPU para deformaciones masivas sin cuello de botella en CPU.

---

## 2. Topología del Ecosistema

```
agents-factory/webgl-sculpt-geometry-ecosystem/
├── README.md
├── .agents/
│   ├── rules/
│   │   └── sculpt-geometry-rules.md
│   └── skills/
│       ├── dyntopo-remesh-specialist/
│       ├── octree-spatial-pipeline-specialist/
│       └── sculpt-brush-dynamics-specialist/
├── brain/
└── knowledge/
    ├── modern_webgpu_sculpt_engine_reference.ts
    └── sculptgl_architecture_and_dyntopo_mastery.md
```

---

## 3. Matriz de Delegación de Subagentes

| Tarea Requerida | Ecosistema Receptor | Subagente / Skill Especializado |
| :--- | :--- | :--- |
| Matemáticas de Pinceles de Escultura, Deformación Radial & Geodésica | `webgl-sculpt-geometry-ecosystem` | `sculpt-brush-dynamics-specialist` |
| Topología Dinámica (Dyntopo), Voxel Remeshing & Dual Contouring | `webgl-sculpt-geometry-ecosystem` | `dyntopo-remesh-specialist` |
| Aceleración Espacial BVH/Octree, Ray Picking & WebGPU Compute Streaming | `webgl-sculpt-geometry-ecosystem` | `octree-spatial-pipeline-specialist` |
| Renderizado PBR de lujo, sombreadores de agua & VFX atmosféricos | `cgi-web-ecosystem` | `web-cgi-rendering-lighting-pipeline-specialist` |
| Reconstrucción y mallas a partir de mapas de profundidad monocular | `sapiens-human-vision-ecosystem` | `sapiens-depth-normal-reconstructor` |
| Rigging esquelético y exportación de modelos terminados a GLB | `blender-ecosystem` | `blender-mcp-automation` |
