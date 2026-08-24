# Reglas Operacionales de Diseño e Ingeniería Frontend Anti-Slop (Taste Skill)

**Alcance:** Todos los entregables visuales, componentes frontend, landing pages y rediseños en Antigravity  
**Normativa:** ISO 25010 (Calidad Estética y Usabilidad), WCAG 2.1 AA/AAA.

---

## 1. Obligación de "Design Read" Previo

1. Ningún agente puede generar código de interfaz sin antes declarar su **Design Read** en una sola línea.
2. La declaración debe especificar:
   - Tipo de página
   - Audiencia objetivo
   - Lenguaje estético
   - Valores calibrados de los 3 diales: `DESIGN_VARIANCE`, `MOTION_INTENSITY`, `VISUAL_DENSITY`.

---

## 2. Prohibición Absoluta de Marcadores de Posición (*Zero-Placeholder Policy*)

1. Queda estrictamente prohibido emitir código con comentarios evasivos como `// TODO: add more cards here`, `/* insert styles */` o `...resto del código`.
2. Todo componente, sección o layout debe entregarse en su totalidad, completamente estilizado y funcional.

---

## 3. Adherencia a Sistemas de Diseño y Restricciones Anti-Slop

1. Si el proyecto ya utiliza un sistema de diseño oficial (Tailwind, Material 3, Radix, shadcn, Carbon), se deben emplear sus tokens nativos sin inventar hacks CSS paralelos.
2. No usar degradados morados genéricos de IA, mallas oscuras centradas ni tres tarjetas idénticas como héroe por defecto.
3. Todo texto interactivo debe tener un contraste mínimo de $4.5:1$ contra su fondo inmediato conforme a WCAG 2.1 AA.
