# Pretext in OpenMontage: Zero-Reflow Video Typography & Subtitle Timing

**Referencia Oficial:** Pretext Engine (*Cheng Lou*)  
**Propósito:** Optimización de renderizado de cartelas tipográficas, textos cinéticos y subtítulos dinámicos en runtimes web-first como `HyperFrames` y `Remotion`, eliminando la latencia de medición de DOM durante la captura headless de fotogramas.

---

## 1. El Reto del Renderizado de Video Headless

En motores de renderizado de video como HyperFrames (basado en Chromium headless), cada fotograma debe capturarse de forma determinista y exacta:
* Si el código de la plantilla invoca `offsetHeight` o `getBoundingClientRect()` para calcular el tamaño de una caja de subtítulos o una cartela animada, Chromium detiene el ciclo de renderizado para ejecutar un reflow síncrono.
* En un video de 60 segundos a 60 FPS (3,600 fotogramas), un reflow de 10ms por frame agrega **36 segundos de tiempo de render muerto**.

---

## 2. Optimización con Pretext en HyperFrames & Angular Video

Al precomputar todos los saltos de línea y alturas de subtítulos con Pretext antes de iniciar la captura de fotogramas:
1. El motor conoce de antemano el número exacto de líneas, las coordenadas de cada palabra y los límites del contenedor.
2. Cada fotograma se dibuja mediante transformaciones CSS o Canvas puras sin tocar APIs de medición.
3. El tiempo de renderizado se reduce en más de un **$40\%$**, garantizando cero parpadeos entre fotogramas.

---

## 3. Ejemplo de Integración en Workspace HyperFrames

```typescript
import { prepare, layout } from 'pretext';

// Pre-render pass: calcular layout de todos los subtítulos del guion
export function precomputeSubtitleLayouts(subtitles: Array<{ text: string, startTime: number, endTime: number }>, maxWidth: number) {
  const font = "bold 48px 'Inter', sans-serif";
  
  return subtitles.map(sub => {
    const prep = prepare(sub.text, font);
    const lines = layout(prep, { maxWidth });
    return {
      ...sub,
      lines,
      totalHeight: lines.length * 56 // altura exacta en píxeles
    };
  });
}
```
