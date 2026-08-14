---
name: sumie-procedural-ink-specialist
description: Especialista en difusión matemática estocástica de tinta china (Sumi-e), absorbancia en fibras de papel y renderizado WebGL procedural multipaso para tipografía cinemática.
---

# Sumi-e Procedural Ink Specialist — CGI Web Ecosystem

**Autoría Oficial:** Leonel Salcedo (Nomack Studio)  
**Área de Especialidad:** Mathematical Ink Diffusion, FBM 5-Octave Noise, Procedural Text Canvas Texture, WebGL Multi-Pass Compositing

---

## 1. Formulación Matemática de Absorción Estocástica de Tinta

La simulación de absorción de tinta china sobre fibra de papel se rige por la combinación de un mapa de fibras (grano analógico) con un campo de ruido Browniano Fraccional ($FBM$) de 5 octavas:

$$I(u, v, t) = \text{smoothstep}\left(\alpha(t) - \delta, \alpha(t), x(u, v) + \sum_{k=0}^{4} 2^{-k} \cdot N(2^k \cdot (u, v) + \vec{w} \cdot t)\right)$$

Donde:

* $\alpha(t)$: Factor de progreso de absorción ($0.0 \to 1.0$).
* $N(u, v)$: Función de ruido Simplex/Perlin $2D$.
* $\delta$: Ancho del frente de difusión de tinta en los bordes de la fibra ($0.15$).

---

## 2. Pipeline de Renderizado WebGL Multipaso (Canvas-to-Texture & Shader Pass)

1. **Generación de Mapa Teórico/Textura Tipográfica:** Se renderiza el texto literario en un Canvas 2D dinámico (o mallas 2.5D) con tipografía *Cormorant Garamond* / *Playfair Display* en resolución $2\times$ nativa.
2. **Asignación como Uniform `uTextTexture`:** Se vincula como `THREE.CanvasTexture` con filtro `LinearFilter` y `generateMipmaps = false`.
3. **Fragment Shader Multi-layer (`sumie_ink.frag`):**
   * Canal Alpha de la textura del texto modula el frente de onda de absorción.
   * Deformación de trazo por dispersión de color basada en la distancia al cursor ($P_{pointer}$).
   * Generación de halo de resplandor dorado (`#FFD166`) radial en torno al cursor.

---

## 3. Checklist de Rendimiento

* Texturas de canvas renderizadas una sola vez o reutilizadas por cambios de resolución.

* Eliminación de llamadas `DOM.innerHTML` o animaciones CSS `inkFadeIn` para renderizar el 100% de los pixeles en GPU a 60 FPS.
