# WHO: Knowledge Base para Agentes de Antigravity
# WHAT: Patrones Matemáticos y Proceduralidad en VFX / Movimientos Orgánicos
# WHEN: Cuando los subagentes deban codificar, parametrizar o solicitar simulaciones orgánicas o sistemas dinámicos.
# WHERE: multimedia-data-ecosystem/knowledge
# WHY: Para anclar la creatividad en bases matemáticas probadas que evitan el "valle inquietante" (uncanny valley) del movimiento digital.

## 1. Generación Procedural y Ruido Matemático
La naturaleza no es un caos puro ni un orden perfecto. Para simularla (agua, terreno, nubes), el CGI utiliza ruidos matemáticos:
- **Ruido de Perlin (Perlin Noise)**: Un algoritmo de generación de texturas de gradiente inventado por Ken Perlin. Crea una pseudo-aleatoriedad suave y continua. Es vital para simular desde el oleaje del mar hasta la distribución de poros en la piel humana.
- **Simplex Noise**: Una evolución del Perlin Noise, computacionalmente más ligero y con menos artefactos direccionales, ideal para 3D y 4D (animación en el tiempo).
- **Fractales (Brownian Motion - fBM)**: Acumulación de múltiples capas (octavas) de ruido a diferentes frecuencias y amplitudes para crear detalles escarpados (como montañas).

## 2. Cinemática y Geometría del Movimiento
Para animaciones orgánicas sin keyframing manual:
- **Cinemática Inversa (IK - Inverse Kinematics)**: Resuelve ecuaciones trigonométricas para determinar cómo deben doblarse las articulaciones "hijas" (codo, hombro) cuando la mano (end-effector) alcanza un punto en el espacio.
- **Coordenadas Baricéntricas**: Sistema matemático usado para interpolar valores dentro de un triángulo. Fundamental para deformar pieles de personajes (skinning) de manera orgánica y sin colapsos de volumen.
- **Ecuaciones de Navier-Stokes**: El pilar de las simulaciones fluidas (agua, humo, fuego). En software procedural (como Houdini), estas ecuaciones calculan la conservación de masa y momentum en cada vóxel (píxel 3D).

## 3. Lógica de Enjambres (Flocking/Crowds)
Los comportamientos orgánicos colectivos (bandadas de pájaros, ejércitos) se basan en el modelo **Boids** de Craig Reynolds, gobernado por tres reglas vectoriales:
1. **Separación**: Evitar chocar con vecinos locales.
2. **Alineación**: Adoptar la dirección promedio del grupo cercano.
3. **Cohesión**: Moverse hacia el centro de masa del vecindario.

*Directriz para Agentes:* Cuando diseñes secuencias CGI dinámicas mediante JSON, especifica estas variables de ruido o lógicas de partículas para asegurar que el modelo generativo o el motor de render aplique física realista y no animación lineal rígida.
