# Pretext Editorial Engine: Zero-Reflow Streaming & Dynamic Spreads

**Referencia Oficial:** Pretext Engine (*Cheng Lou*)  
**Propósito:** Patrón de ingeniería y diseño UI/UX para interfaces editoriales de alta gama, diagramación dinámica tipo revista (*editorial spreads*), masonry grids ultra-rápidos y streaming de texto generado por IA sin saltos de scroll (*scroll jump*) ni sobrecarga de reflow.  
**Cumplimiento Normativo:** ISO 25010 (Calidad y Eficiencia de Software), ISO 9241-110 (Diálogo Ergonómico), WCAG 2.1 AA/AAA.

---

## 1. Casos de Uso Clave en UI/UX de Vanguardia

### 1.1. Streaming de Tokens de IA (Chatbots & Asistentes Generativos)
* **Problema Tradicional:** Cada nuevo token emitido por el LLM hace mutar el DOM y obliga al navegador a recalcular el tamaño del contenedor, provocando parpadeos y desincronización del scroll automático.
* **Solución con Pretext:** A medida que los tokens llegan, `prepare()` procesa los nuevos segmentos y `layout()` proyecta la altura exacta de la burbuja en memoria, fijando la posición del scroll de forma suave y sin *layout shifts*.

### 1.2. Editorial Spreads & Obstacle-Aware Grids (Revistas Digitales de Lujo)
* Permite crear páginas de altura fija donde el texto fluye fluidamente entre múltiples columnas, rodeando imágenes flotantes, citas destacadas (*pull quotes*) o videos interactivos sin necesidad de hacks de CSS complejos o cálculos lentos con JavaScript.

---

## 2. Implementación de Referencia en Componentes de Diseño

```typescript
import { prepare, layout } from 'pretext';

export class EditorialColumnLayout {
  private preparedContent: any;

  constructor(private rawText: string, private fontStyle: string) {
    // Fase 1: Medición en memoria (ejecutada solo al cambiar el contenido)
    this.preparedContent = prepare(this.rawText, this.fontStyle);
  }

  public computeColumnFlow(columnWidth: number, obstacles: Array<{ x: number, y: number, width: number, height: number }>) {
    // Fase 2: Pura aritmética (~0.05ms)
    return layout(this.preparedContent, {
      maxWidth: columnWidth,
      obstacles
    });
  }
}
```

---

## 3. Checklist de Decisión: Cuándo Adoptar Pretext

- [ ] ¿La interfaz requiere texto fluido rodeando elementos dinámicos a 60 FPS? ➔ **USAR PRETEXT**.
- [ ] ¿Hay streaming continuo de texto con necesidad de altura predictiva? ➔ **USAR PRETEXT**.
- [ ] ¿Es una página corporativa estándar con layout estático en CSS Grid/Flexbox? ➔ **NO USAR PRETEXT (Usar CSS nativo)**.
- [ ] ¿Se requiere que el texto siga siendo 100% accesible para lectores de pantalla? ➔ **CUMPLIDO (Renderiza nodos semánticos en el DOM)**.
