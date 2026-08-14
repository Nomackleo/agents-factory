# Playdead INSIDE Engine Technical Reference: Rendering & Volumetrics Breakdown

## 1. Contexto Técnico

En la conferencia SIGGRAPH / GDC, Playdead detalló las técnicas gráficas que otorgaron a *INSIDE* su estética atmosférica y cinematográfica inconfundible. Esta referencia compila los algoritmos centrales adaptados para WebGL2 y WebGPU.

---

## 2. Pilares de Renderizado

### A. Temporal Reprojection Anti-Aliasing (TAA) & Volumetrics

- **Problema:** El raymarching de niebla 3D a resolución nativa es prohibitivo para 60 FPS en Web.
- **Solución INSIDE:** Evaluar la niebla volumétrica a $1/2$ o $1/4$ de resolución con sólo 16-32 pasos por rayo, aplicando un *jittering* pseudo-aleatorio por frame (secuencia Halton / Blue Noise).
- **Reproyección Temporal:** Cada frame mezcla el resultado actual con el historial del buffer anterior usando vectores de velocidad (Motion Vectors).
- **Fórmula de Mezcla Temporal:**
  $$\text{Fog}_{\text{final}} = \alpha \cdot \text{Fog}_{\text{current}} + (1 - \alpha) \cdot \text{Fog}_{\text{reprojected}}, \quad \alpha \approx 0.05$$

### B. Directional Volumetric Shadows & God Rays

- **Phase Function (Mie Scattering):** Utiliza la función Henyey-Greenstein para simular dispersión hacia adelante (*forward scattering*):
  $$P(\theta) = \frac{1 - g^2}{4\pi (1 + g^2 - 2g \cos\theta)^{1.5}}, \quad g \in [0.6, 0.85]$$
- **Shadow Map Integration:** En cada paso del raymarcher, se transforma la posición 3D al espacio de luz para consultar la textura de sombras (CSM), bloqueando los rayos eclipsados por la geometría.

### C. Atmospheric Height Fog

- **Densidad Exponencial:** La niebla se vuelve más densa cerca del suelo/agua:
  $$\rho(y) = \rho_0 \cdot e^{-h \cdot y}$$
- Permite capas de bruma flotante sobre superficies húmedas o agua.

### D. Screen-Space Contact Shadows

- Complementa los shadow maps tradicionales con raymarching rápido en Screen Space (Profundidad de pantalla) para micro-sombras en los pies del personaje, ropa y grietas.

### E. Ópticas Subacuáticas & Cáusticas 3D

- **Absorción de Luz (Beer-Lambert):** La luz roja se absorbe primero, dejando tonos azulados/verdosos profundos:
  $$I(d) = I_0 \cdot e^{-\sigma_{\text{abs}} \cdot d}$$
- **Cáusticas Procedurales 3D:** Proyección de campos de altura de ruido Voronoi/Simplex combinados con animación temporal en el volumen de agua.
