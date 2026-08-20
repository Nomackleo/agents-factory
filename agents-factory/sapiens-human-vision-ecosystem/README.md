# Sapiens Human Vision Ecosystem — Universal Antigravity Architecture

**Autoría Oficial:** Leonel Salcedo (Nomack Studio)  
**WHAT**: Ecosistema Agéntico Dedicado para la Visión Humana por IA, Captura de Movimiento (MoCap) 3D sin marcadores, Estimación de Poses (308 keypoints), Reconstrucción de Profundidad y Normales de Superficie a resolución 1K (1024x1024), Segmentación Anatómica Fina y Pipelines de Inferencia Acelerada basados en **Meta Sapiens** (`facebookresearch/sapiens`).  
**Cumplimiento Normativo:** ISO 9001:2015, ISO 42001 (AIMS - Artificial Intelligence Management System), ISO 27001 (ISMS), NIST CSF 2.0, DORA & `implicit/`.

---

## 1. Misión y Alcance del Ecosistema

El **Sapiens Human Vision Ecosystem** encapsula los modelos fundacionales de Meta Reality Labs entrenados sobre 300 millones de imágenes humanas para transformar fotografías y videos 2D en datos espaciales 3D de alta fidelidad:

1. **Digitalización Humana:** Conversión de imágenes mononucleares en mallas 3D, mapas de normales para sombreado PBR y mapas de profundidad métrica para NeRF y 3D Gaussian Splatting.
2. **Animación y MoCap para 3D Web:** Extracción precisa de 308 keypoints (cuerpo, dedos de manos, rostro y pies) para alimentar avatares en WebGL2, WebGPU, Three.js, Blender y WebXR.
3. **Efectos Visuales (VFX) & Virtual Try-On:** Segmentación semántica de 28 clases anatómicas para cambio de ropa procedural, aislamiento de actores y composición cinematográfica.

---

## 2. Topología del Ecosistema

```
agents-factory/sapiens-human-vision-ecosystem/
├── README.md
├── .agents/
│   ├── rules/
│   │   └── sapiens-rules.md
│   └── skills/
│       ├── sapiens-bodypart-segmentation-specialist/
│       ├── sapiens-depth-normal-reconstructor/
│       ├── sapiens-lite-inference-optimizer/
│       └── sapiens-pose-mocap-specialist/
├── brain/
└── knowledge/
    ├── meta_sapiens_foundation_architecture.md
    └── sapiens_inference_pipeline_recipes.py
```

---

## 3. Matriz de Delegación de Subagentes

| Tarea Requerida | Ecosistema Receptor | Subagente / Skill Especializado |
| :--- | :--- | :--- |
| Extracción de Pose 2D/3D, Tracking de 308 Keypoints & MoCap | `sapiens-human-vision-ecosystem` | `sapiens-pose-mocap-specialist` |
| Reconstrucción de Profundidad Métrica & Normales 3D a 1K | `sapiens-human-vision-ecosystem` | `sapiens-depth-normal-reconstructor` |
| Segmentación Anatómica de 28 Clases, Parsing Corporal & VFX | `sapiens-human-vision-ecosystem` | `sapiens-bodypart-segmentation-specialist` |
| Optimización TorchScript/TensorRT, Inferencia 4x Sapiens-Lite | `sapiens-human-vision-ecosystem` | `sapiens-lite-inference-optimizer` |
| Renderizado WebGL/WebGPU de avatares y mallas resultantes | `cgi-web-ecosystem` | `threejs-webgpu-tsl-architect` |
| Rigging de esqueletos, L-Systems y exportación GLB en Blender | `blender-ecosystem` | `blender-mcp-automation` |
| Integración WebXR en Meta Quest / Visores de Realidad Virtual | `cgi-web-ecosystem` | `webxr-immersive-experience-specialist` |
