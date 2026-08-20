# Meta Sapiens — Arquitectura de Modelos Fundacionales para Visión Humana

**Referencia Oficial:** Meta Reality Labs (`facebookresearch/sapiens`) — ECCV 2024 Best Paper Candidate  
**Autores Principales:** Rawal Khirodkar, Timur Bagautdinov, Julieta Martinez, Shunsuke Saito et al.  
**Pre-entrenamiento:** Masked Autoencoders (MAE) sobre 300 millones de imágenes humanas (*Humans-300M*) a resolución nativa de 1024x1024 (16x16 patch size).

---

## 1. Familia de Modelos y Tamaños

| Modelo | Parámetros | Dimensiones Embedding | Capas ViT | Atención Heads | Caso de Uso Óptimo |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`Sapiens-0.3B`** | 336M | 1024 | 24 | 16 | Tiempo Real / Edge GPUs / WebSockets / MoCap en vivo |
| **`Sapiens-0.6B`** | 672M | 1280 | 32 | 16 | Producción estándar / Excelente balance precisión-velocidad |
| **`Sapiens-1B`** | 1.13B | 1536 | 40 | 24 | Alta Fidelidad / Reconstrucción de avatares fotorrealistas |
| **`Sapiens-2B`** | 2.05B | 1920 | 48 | 32 | Renderizado cinematográfico / Calibración de datasets |

---

## 2. Las 4 Tareas Fundacionales Human-Centric

```
                       ┌────────────────────────────────────────┐
                       │     Sapiens ViT-MAE Backbone (1K)      │
                       └───────────────────┬────────────────────┘
                                           │
         ┌──────────────────┬──────────────┴─────┬──────────────────┐
         ▼                  ▼                    ▼                  ▼
  [ 2D/3D Pose ]      [ Depth 3D ]         [ Normals 3D ]     [ Segmentation ]
  - 308 Keypoints     - Metric Depth       - Surface Vectors  - 28 Classes
  - Body + Face +     - Relative Depth     - PBR Tangent      - Apparel + Hair
    Hands + Feet      - 1024x1024 Res        Normals 1K         + Body Parts
```

### A. Estimación de Pose (308 Keypoints)
Sapiens supera los esquemas clásicos de COCO (17 puntos) u OpenPose al predecir **308 puntos anatómicos articulados**:
* **Cuerpo Principal:** 24 puntos (cabeza, cuello, hombros, codos, muñecas, caderas, rodillas, tobillos).
* **Rostro Denso:** 68 puntos (contorno mandibular, cejas, ojos, nariz, labios).
* **Manos (Bimanual):** 42 puntos (21 articulaciones por mano: carpos, metacarpofalángicas, interfalángicas).
* **Pies y Calzado:** 6 puntos (talón, metatarso, dedo gordo).
* **Superficie Corporal:** 168 puntos de muestreo en torso y extremidades para deformación de mallas.

### B. Segmentación de Partes del Cuerpo (28 Clases)
Clasificación semántica a nivel de píxel:
1. Fondo, 2. Piel Rostro, 3. Labio Superior, 4. Labio Inferior, 5. Dientes, 6. Lengua, 7. Ojo Izquierdo, 8. Ojo Derecho, 9. Ceja Izquierda, 10. Ceja Derecha, 11. Oreja Izquierda, 12. Oreja Derecha, 13. Cabello, 14. Cuello, 15. Torso / Piel Superior, 16. Brazo Izquierdo, 17. Brazo Derecho, 18. Mano Izquierda, 19. Mano Derecha, 20. Pierna Izquierda, 21. Pierna Derecha, 22. Pie Izquierdo, 23. Pie Derecho, 24. Ropa Superior, 25. Ropa Inferior, 26. Vestido / Traje, 27. Zapatos, 28. Accesorios (sombreros, bolsos).

### C. Profundidad Métrica y Normales 3D a 1024x1024
* **Mapas de Profundidad:** Estimación directa de la distancia cámara-superficie en metros, permitiendo generar mallas 3D tridimensionales directas con proyección de cámara inversa.
* **Mapas de Normales:** Orientación espacial $\vec{n} = (n_x, n_y, n_z)$ en cada píxel para recrear micro-arrugas de la ropa y geometría facial en sombreadores WebGL/Three.js.

---

## 3. Sapiens-Lite: Pipeline de Inferencia Ultrarrápido (4x Speedup)

Sapiens-Lite desacopla el modelo de los frameworks pesados de entrenamiento, ejecutándose sobre **TorchScript** puro:

```python
import torch
import cv2
import numpy as np

# 1. Cargar modelo TorchScript optimizado
model = torch.jit.load("sapiens_0.3b_normal_render_bfloat16.pt2", map_location="cuda")
model.eval()

# 2. Preprocesamiento a 1024x1024
img = cv2.imread("human.jpg")
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_resized = cv2.resize(img_rgb, (1024, 1024))
input_tensor = torch.from_numpy(img_resized).permute(2, 0, 1).unsqueeze(0).float() / 255.0

# Normalización ImageNet
mean = torch.tensor([0.485, 0.456, 0.406]).view(1, 3, 1, 1)
std = torch.tensor([0.229, 0.224, 0.225]).view(1, 3, 1, 1)
input_tensor = ((input_tensor - mean) / std).cuda().to(torch.bfloat16)

# 3. Inferencia ultrarrápida
with torch.inference_mode():
    output = model(input_tensor)
```

---

## 4. Reconstrucción de Mallas 3D Manifold (Dual Contouring & SurfaceNets)

Integrando las técnicas de [`webgl-sculpt-geometry-ecosystem`](file:///c:/Users/Nomack/Documents/workspace/agents/antigravity/dev/prompt-generator/agents-factory/webgl-sculpt-geometry-ecosystem), los mapas de profundidad métrica y normales monoculares de Meta Sapiens se convierten en **mallas 3D sólidas, estancas (*watertight*) y con topología 2-manifold**:

1. **Back-projection de Píxeles a Espacio 3D:**
   $$\mathbf{P}(u, v) = \mathbf{K}^{-1} \begin{bmatrix} u \\ v \\ 1 \end{bmatrix} \cdot \text{Depth}(u, v)$$
2. **Volumetría SDF / Voxel Grid:** Conversión de la nube de puntos densa en un campo de distancias con signo (*Signed Distance Field*).
3. **Extracción Isosuperficial (Manifold Dual Contouring):** Resuelve matrices QEF (Quadric Error Functions) utilizando los vectores normales estimados por Sapiens para posicionar vértices con aristas afiladas y contornos faciales limpios.
4. **Exportación a Three.js / Blender:** Generación directa de archivos `.glb` con mapas de normales en espacio tangente integrados.

