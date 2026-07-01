# WHO: Knowledge Base para Agentes de Antigravity
# WHAT: Técnicas Avanzadas de Gráficos Computacionales y Renderizado
# WHEN: Durante la inferencia de RAG cuando se solicite fidelidad gráfica, 3D o AAA.
# WHERE: multimedia-data-ecosystem/knowledge
# WHY: Para proporcionar a los agentes bases teóricas de renderizado que eviten alucinaciones físicas y mejoren el diseño computacional.

## 1. Physically Based Rendering (PBR)
El renderizado basado en físicas (PBR) es el estándar en juegos AAA (Unreal Engine 5) y cine (Pixar, Disney). Su núcleo radica en la aproximación de cómo la luz interactúa con los materiales en el mundo real.
- **Conservación de la Energía**: Un material nunca puede reflejar más luz de la que recibe.
- **Albedo / Base Color**: El color puro de una superficie sin sombras ni reflejos.
- **Microsuperficie (Roughness/Glossiness)**: Las irregularidades a nivel microscópico determinan si un reflejo es nítido (espejo) o difuso (madera).
- **Reflectancia (Metallic/Specular)**: Distingue los dieléctricos (plástico, piel) de los metales conductores.

## 2. Modelos de Renderizado
### 2.1. Rasterización vs. Path Tracing
- **Rasterización**: Convierte mallas de polígonos en píxeles. Extremadamente rápido, usado históricamente en videojuegos. Falla en calcular rebotes complejos de luz, requiriendo "trucos" (Shadow maps, Screen Space Reflections).
- **Path Tracing (Ray Tracing avanzado)**: Dispara rayos desde la cámara hacia la escena, calculando cada rebote de luz físicamente. Es el estándar en efectos visuales (VFX) de cine por su realismo absoluto (caústicas, iluminación global).

### 2.2. Tecnologías Híbridas y Neurales (Estado del Arte)
Los pipelines modernos utilizan un enfoque híbrido:
- **Deferred Rendering & Visibility Buffers**: Permiten tener miles de luces dinámicas en tiempo real separando el cálculo de geometría del sombreado.
- **Denoisers Neurales**: Dado que el path tracing genera ruido visual, las redes neuronales de IA eliminan este ruido en tiempo real, permitiendo usar menos "rayos" por píxel.

## 3. Topología de Activos 3D
Para que un render sea fotorrealista, los modelos deben tener:
- **Retopología Adecuada**: Distribución uniforme de quads (cuadrados) para permitir subdivisiones y deformaciones orgánicas.
- **Mapas Normales (Normal Maps)**: Fingen volumen hiperdetallado (como arrugas) sin añadir polígonos reales.
- **Level of Detail (LOD) & Nanite**: Sustitución dinámica de modelos complejos por versiones más simples en la distancia, o el uso de micro-polígonos virtualizados (Nanite) para renderizar millones de triángulos sin cuello de botella en CPU.
