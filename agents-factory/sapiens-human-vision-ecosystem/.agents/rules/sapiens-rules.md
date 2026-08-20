# Reglas Operacionales del Ecosistema Sapiens Human Vision

**Alcance:** Modelos Fundacionales Meta Sapiens (Pose, Depth, Normal, Segmentation)  
**Normativa:** ISO 42001 (AIMS), ISO 25010 (Eficiencia de Recursos & Fiabilidad), DORA.

---

## 1. Reglas de Inferencia y Normalización de Entradas

1. **Resolución Nativa de Inferencia:**
   - Todas las imágenes de entrada deben ser redimensionadas a **1024x1024** píxeles con preservación de aspect ratio y *padding* simétrico (letterboxing) para evitar distorsiones anatómicas en el ViT.
2. **Normalización de Tensores:**
   - Media: `[0.485, 0.456, 0.406]`
   - Desviación Estándar: `[0.229, 0.224, 0.225]`
   - Espacio de Color: `RGB` en rango `[0.0, 1.0]`.

---

## 2. Gestión de Memoria GPU & Checkpoints

1. **Estrategia Sapiens-Lite por Defecto:**
   - Para despliegues en servidores o estaciones de trabajo estándar, priorizar checkpoints **TorchScript exportados (`.pt2` / `.torchscript`)** de `sapiens_0.3b` o `sapiens_0.6b` con inferencia FP16.
2. **Uso de Checkpoints Grandes (`sapiens_1b`, `sapiens_2b`):**
   - Reservados exclusivamente para tareas de renderizado offline, *high-end VFX* o entrenamiento/finetuning con VRAM > 24GB.
3. **Limpieza de VRAM:**
   - Siempre invocar `torch.cuda.empty_cache()` y destruir tensores intermedios tras lotes grandes de video.

---

## 3. Compatibilidad de Salida con el Ecosistema 3D

1. **Formato de Poses:** Coordenadas normalizadas $(x, y, c)$ para los 308 keypoints, exportables a JSON/BVH para consumo directo en Three.js o Blender.
2. **Formato de Normales:** Mapas RGB de 16-bit o 8-bit donde $[R, G, B] = \frac{\vec{n} + 1.0}{2.0} \cdot 255$.
3. **Formato de Profundidad:** Imágenes flotantes de 32-bit (EXR/TIFF) o PNG normalizado para displacement maps en Three.js.
4. **Formato de Segmentación:** Máscaras booleanas de 8-bit o tensores con índices enteros del 0 al 27.
