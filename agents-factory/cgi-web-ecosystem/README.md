# CGI Web Ecosystem — Universal Antigravity Architecture

**Autoría Oficial:** Leonel Salcedo (Nomack Studio)  
**WHAT**: Ecosistema Agéntico Reutilizable para la creación de experiencias web inmersivas de alta fidelidad, motores gráficos WebGL/WebGPU, sombreadores GLSL impresionistas, dinámicas de partículas en GPU (Curl Noise) y pipelines de post-procesado multipaso.  
**Cumplimiento Normativo:** ISO 9001:2015, ISO 42001 (AIMS), ISO 27001 (ISMS), NIST CSF 2.0, DORA & `implicit/`

---

## 1. Misión y Alcance Multiproyecto

El **CGI Web Ecosystem** encapsula los roles, pipelines y habilidades agénticas especializadas para desarrollar experiencias 3D/2.5D de nivel comercial de lujo (estilo Immersive Garden / Cartier in Time / Active Theory).

Se desacopla totalmente de entregables específicos y se reutiliza a través de múltiples proyectos en `projects/` (ej. `projects/homenaje-madre`, `projects/nomackstudio-landing`, etc.).

---

## 2. Topología del Ecosistema

```
agents-factory/cgi-web-ecosystem/
├── README.md
├── .agents/
│   ├── rules/
│   │   └── cgi-web-rules.md
│   └── skills/
│       ├── curl-noise-vfx-specialist/
│       ├── glsl-shader-architect/
│       ├── inside-engine-atmosphere-specialist/
│       ├── sumie-procedural-ink-specialist/
│       ├── webgl-high-perf-engine/
│       └── web-cgi-rendering-lighting-pipeline-specialist/
├── brain/
└── knowledge/
```

---

## 3. Matriz de Delegación de Subagentes

| Tarea Requerida | Ecosistema Receptor | Subagente / Skill Especializado |
| :--- | :--- | :--- |
| Pipeline de renderizado multipaso (Deferred/Forward+), IBL & PCSS | `cgi-web-ecosystem` | `web-cgi-rendering-lighting-pipeline-specialist` |
| Niebla volumétrica raymarched, God Rays, TAA & ópticas INSIDE | `cgi-web-ecosystem` | `inside-engine-atmosphere-specialist` |
| Simulación de partículas incompresibles en GPU | `cgi-web-ecosystem` | `curl-noise-vfx-specialist` |
| Sombreadores Sumi-e, acuarela & Sobel filters | `cgi-web-ecosystem` | `glsl-shader-architect` |
| Tinta procedural Sumi-e & lienzo japonés | `cgi-web-ecosystem` | `sumie-procedural-ink-specialist` |
| Optimización de 60 FPS & degradación adaptativa | `cgi-web-ecosystem` | `webgl-high-perf-engine` |
| Modelado 3D, L-Systems, Morph Targets & Draco GLB | `blender-ecosystem` | `blender-mcp-automation` |
| Refactorización de código limpio & LOC (-54%) | `minimal-coding-ecosystem` | `minimal-code-refactorer` |
| Documentación técnica & ISO/NIST compliance | `docs-as-code-ecosystem` | `docs-architect` |
