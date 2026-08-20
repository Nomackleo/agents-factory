# Arquitectura de Simulación de Fluidos GPGPU & Shaders de Agua en Tiempo Real

**Autoría & Referencia Base:** Leonel Salcedo (`lln_clarity_depth` / El Velo de la Percepción: Clarity & Depth)  
**Técnica Fundamental:** Simulación de Heightfield por Diferencias Finitas (Método Evan Wallace) + Pipeline Multipaso en GPU (WebGL2 / Three.js / WebGPU).  
**Cumplimiento Normativo:** ISO 25010 (Eficiencia de Rendimiento & Mantenibilidad), DORA (Garantía de 60+ FPS fijos).

---

## 1. Fundamentos Matemáticos y Arquitectura GPGPU

### A. Ecuación de Onda 2D Discretizada

La propagación de ondas superficiales en un medio elástico o líquido incompresible de profundidad constante se rige por la ecuación diferencial de onda bidimensional:

$$\frac{\partial^2 u}{\partial t^2} = c^2 \nabla^2 u = c^2 \left( \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} \right)$$

Donde:

* $u(x, y, t)$ representa la altura de la columna de agua en el punto $(x,y)$ en el tiempo $t$.
* $c$ es la velocidad de propagación de la onda ($\text{WAVE\_SPEED} \approx 0.85$).
* $\nabla^2 u$ es el operador Laplaciano en 2D.

Discretizando mediante el método de diferencias finitas centrado sobre una grilla regular con espaciado $\Delta x = \Delta y$:

$$\nabla^2 u_{i,j} \approx u_{i+1,j} + u_{i-1,j} + u_{i,j+1} + u_{i,j-1} - 4 u_{i,j}$$

La altura en el siguiente paso de tiempo $t + \Delta t$ se calcula como:

$$u_{i,j}^{t+\Delta t} = 2 u_{i,j}^t - u_{i,j}^{t-\Delta t} + c^2 \Delta t^2 \nabla^2 u_{i,j}^t$$

Aplicando un factor de amortiguación progresivo $\gamma \in (0, 1)$ (típicamente $0.995 - 0.996$) para simular disipación viscosa:

$$u_{i,j}^{t+\Delta t} = \left( 2 u_{i,j}^t - u_{i,j}^{t-\Delta t} + c^2 \Delta t^2 \nabla^2 u_{i,j}^t \right) \cdot \gamma$$

---

## 2. Pipeline de Simulación Ping-Pong en GPU

```
[ RenderTarget A ] (Lectura: Altura Actual 'r' y Previa 'g')
        │
        ▼ (Shader de Simulación: updateFragment.glsl)
[ RenderTarget B ] (Escritura: Nueva Altura 'r' y Altura Actual 'g')
        │
        ▼ (Swap / Intercambio de punteros A <-> B)
[ RenderTarget B ] pasa a ser Lectura en el siguiente frame
```

### Canales de la Textura de Simulación (RGBA HalfFloat / UnsignedByte)

* **Canal R (`.r`):** Altura calculada en el paso actual $u(t)$.
* **Canal G (`.g`):** Altura del paso anterior $u(t-1)$ (conservada para calcular la derivada temporal de segundo orden).
* **Canal B (`.b`):** Desplazamiento adicional / espuma / perturbaciones.
* **Canal A (`.a`):** 1.0.

---

## 3. Desacoplamiento de Física con Fixed Timestep (120 Hz)

Para evitar que la velocidad de propagación de las ondas varíe según la tasa de refresco del monitor del usuario (60Hz, 120Hz, 144Hz, 240Hz) o sufra colapsos (*spiral of death*), la física se ejecuta en pasos de tiempo fijos:

```typescript
const fixedTimeStep = 1 / 120; // 120 Hz
const maxSubSteps = 4;
let accumulator = 0;

function animate(deltaTime: number) {
  accumulator += deltaTime;
  let subSteps = 0;
  
  while (accumulator >= fixedTimeStep && subSteps < maxSubSteps) {
    waterSimulator.update();
    accumulator -= fixedTimeStep;
    subSteps++;
  }
}
```

---

## 4. Shaders Centrales de Simulación (GLSL ES)

### A. Shader de Actualización de Onda (`updateFragment.glsl`)

```glsl
precision highp float;

uniform sampler2D u_texture;
uniform vec2 u_delta;
uniform float u_damping;

const float WAVE_SPEED = 0.85;
const float BOUNDARY_DAMPING = 0.85;
const float MIN_HEIGHT = -0.08;
const float MAX_HEIGHT = 0.08;

void main() {
    vec2 uv = gl_FragCoord.xy * u_delta;
    
    if (uv.x <= 0.0 || uv.x >= 1.0 || uv.y <= 0.0 || uv.y >= 1.0) {
        gl_FragColor = vec4(0.0, 0.0, 0.0, 1.0);
        return;
    }
    
    vec4 currentSample = texture2D(u_texture, uv);
    float currentHeight = currentSample.r;
    float previousHeight = currentSample.g;
    
    float north = texture2D(u_texture, uv + vec2(0.0, u_delta.y)).r;
    float south = texture2D(u_texture, uv - vec2(0.0, u_delta.y)).r;
    float east  = texture2D(u_texture, uv + vec2(u_delta.x, 0.0)).r;
    float west  = texture2D(u_texture, uv - vec2(u_delta.x, 0.0)).r;
    
    vec2 edgeDistance = min(uv, 1.0 - uv);
    float edgeFactor = min(edgeDistance.x, edgeDistance.y);
    float boundaryDamping = smoothstep(0.0, u_delta.x * 4.0, edgeFactor);
    
    float laplacian = (north + south + east + west - 4.0 * currentHeight);
    float c2dt2 = WAVE_SPEED * WAVE_SPEED * 0.3;
    float newHeight = 2.0 * currentHeight - previousHeight + c2dt2 * laplacian;
    
    newHeight *= mix(BOUNDARY_DAMPING, u_damping, boundaryDamping);
    newHeight = clamp(newHeight, MIN_HEIGHT, MAX_HEIGHT);
    
    gl_FragColor = vec4(newHeight, currentHeight, 0.0, 1.0);
}
```

### B. Inyección de Gotas / Interacción del Puntero (`dropFragment.glsl`)

```glsl
precision highp float;

uniform sampler2D u_texture;
uniform vec2 u_center;
uniform float u_radius;
uniform float u_strength;
uniform vec2 u_delta;

void main() {
    vec2 uv = gl_FragCoord.xy * u_delta;
    vec4 info = texture2D(u_texture, uv);
    
    float drop = max(0.0, 1.0 - length(u_center - uv) / u_radius);
    drop = 0.5 - cos(drop * 3.14159265359) * 0.5;
    info.r += drop * u_strength;
    
    gl_FragColor = info;
}
```

---

## 5. Pipeline de Renderizado Multipaso de Superficie y Cáusticas

```
Paso 1: Pase de Refracción (Offscreen RenderTarget sin la malla de agua)
        │
Paso 2: Pase de Simulación Ping-Pong (GPGPU Heightfield)
        │
Paso 3: Pase de Cáusticas (Cámara Ortográfica proyectando gradientes al lecho)
        │
Paso 4: Pase Principal (Malla de agua con Refracción Snell + Normal Sobel 3x3 + Fresnel)
```

### Shader de Superficie de Agua (`waterFragment.glsl`)

* **Derivación de Normales en GPU:** Kernel Sobel 3x3 sobre el mapa de alturas para calcular $\nabla u = \left(\frac{\partial u}{\partial x}, \frac{\partial u}{\partial z}\right)$ y $\vec{n} = \text{normalize}(-2\cdot dx, 1.0, -2\cdot dz)$.
* **Refracción de Snell:** $\vec{v}_{\text{refract}} = \text{refract}(\vec{v}_{\text{view}}, \vec{n}, 1.0 / 1.33)$.
* **Efecto Fresnel:** $F = (1 - |\vec{v}_{\text{view}} \cdot \vec{n}|)^3$ para mezclar el color superficial del agua con la luz refractada del fondo.
* **Especularidad Blinn-Phong:** $\vec{h} = \text{normalize}(\vec{l} - \vec{v}_{\text{view}})$, $I_{\text{spec}} = (\max(\vec{n} \cdot \vec{h}, 0.0))^{\text{shininess}}$.

---

## 6. Heurísticas de Mitigación para GPUs Móviles (Android Low-Cap & iOS)

1. **Texel Snapping:** En GPUs de baja precisión (ej. Mali / Adreno básicas), redondear las coordenadas UV al centro del texel para suprimir el temblor (*shimmer*):
   $$\text{UV}_{\text{snapped}} = \frac{\lfloor \text{UV} \cdot \text{Res} + 0.5 \rfloor}{\text{Res}}$$
2. **Amortiguación de Gradientes Fuertes:**
   $$\text{damping} = \frac{1.0}{1.0 + |\nabla u|^2 \cdot 0.75}$$
3. **Blur 5-Tap en Refracción:** Distribución Poisson simplificada sobre el buffer de refracción para disimular aliasing de píxel.
4. **Formato de Texturas:** Fallback automático a `THREE.UnsignedByteType` con `LinearFilter` si `HalfFloatType` no tiene soporte de render target o filtrado lineal en el dispositivo cliente.
