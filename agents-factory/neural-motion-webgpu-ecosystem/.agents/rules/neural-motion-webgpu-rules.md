# Reglas Operativas y Estándares de Diseño: Neural Motion WebGPU Ecosystem

**Propósito:** Definir los estándares inmutables para la síntesis de animación neuronal (AI4Animation / PFNN / MANN), inferencia de tensores en Compute Shaders de WebGPU, cinemática inversa (IK) para bloqueo de pies y retargeting esquelético en tiempo real a 60–120 FPS.  
**Cumplimiento Normativo:** W3C WebGPU Standard, ISO 25010 (Eficiencia de Rendimiento y Latencia Ultrabaja), ISO 42001 (AIMS).

---

## 1. Reglas de Inferencia Neuronal en WebGPU

1. **Ejecución Asíncrona en GPU (Compute Shaders / WGSL):**
   - La multiplicación de matrices densas de la red neuronal ($W \times X + B$) debe ejecutarse mediante Compute Shaders en WGSL dentro de la GPU para evitar cuellos de botella en la CPU del navegador.
2. **Representación de Pesos Tensoriales:**
   - Los pesos de la red neuronal deben cargarse desde búferes binarios empaquetados (`.bin` en `Float32Array`) con un tamaño objetivo menor a $20\text{MB}$ para garantizar tiempos de carga web instantáneos.
3. **Frecuencia de Actualización e Interpolación:**
   - El bucle neuronal debe operar a una frecuencia de muestreo de $16\text{Hz}$ a $60\text{Hz}$ con interpolación esférica de cuaterniones (SLERP) para transiciones fluidas entre fotogramas.

---

## 2. Reglas Cinemáticas y Retargeting Esquelético

1. **Jerarquía de Huesos Estandarizada:**
   - Las rotaciones locales deben expresarse exclusivamente en cuaterniones normalizados $[x, y, z, w]$ para prevenir el bloqueo de cardán (*Gimbal Lock*).
2. **Bloqueo de Pies y Cinemática Inversa (Foot-Contact IK):**
   - Para erradicar el deslizamiento de pies (*foot sliding*), la red debe predecir la probabilidad de contacto con el suelo ($P_{\text{contact}} \ge 0.5$). Cuando hay contacto, aplicar corrección Two-Bone IK en tobillo y rodilla.
3. **Predicción de Trayectoria del Personaje:**
   - El vector de entrada debe incluir la trayectoria futura estimada en ventanas de $0.2\text{s}$, $0.4\text{s}$ y $0.8\text{s}$ para anticipar giros, aceleraciones y paradas realistas.

---

## 3. Gobernanza de Licencias y Cohesión de Ecosistema

1. **Atribución y Cumplimiento:**
   - Reconocer la autoría fundacional de la arquitectura AI4Animation (Sebastian Starke & Paul Starke / CC BY-NC 4.0).
2. **Cero Duplicidad con Visión Computacional:**
   - Delegar la extracción de MoCap de video a `sapiens-human-vision-ecosystem`; el motor `neural-motion-webgpu-ecosystem` se enfoca estrictamente en la síntesis e inferencia interactiva.
