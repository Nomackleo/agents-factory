# Especificación Maestra `DESIGN.md` — Identidad Visual Estructurada para Agentes de Código

**Referencia Oficial:** `Nomackleo/design.md`  
**Objetivo:** Proporcionar a los agentes de IA un entendimiento persistente, estructurado y matemáticamente verificable de un sistema de diseño e identidad visual combinando **tokens legibles por máquina (YAML front matter)** con **justificación estética humana (Markdown prose)**.  
**Cumplimiento Normativo:** WCAG 2.1 (AA / AAA), ISO 9241-110 (Ergonomía de Interacción), ISO 25010 (Usabilidad y Accesibilidad).

---

## 1. Estructura Dual de un Archivo `DESIGN.md`

Un archivo `DESIGN.md` se compone estrictamente de dos capas complementarias:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                             Archivo DESIGN.md                               │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. YAML Front Matter (Delimitado por ---):                                  │
│    Valores normativos exactos: colors, typography, rounded, spacing,        │
│    elevation, components.                                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│ 2. Markdown Body (Prosa estructurada en secciones ##):                      │
│    ## Overview, ## Colors, ## Typography, ## Components, ## Atmospheric     │
│    Explicación semántica del por qué de las decisiones y reglas de uso.     │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Esquema Formal de Tokens YAML

```yaml
---
name: Heritage
colors:
  primary: "#1A1C1E"
  on-primary: "#FFFFFF"
  secondary: "#6C7278"
  on-secondary: "#FFFFFF"
  tertiary: "#B8422E"
  neutral: "#F7F5F2"
  surface: "#FFFFFF"
  on-surface: "#1A1C1E"
  surface-container: "#F0ECE6"
  outline: "#D1CBC3"
  error: "#BA1A1A"
typography:
  display-lg:
    fontFamily: "Public Sans, sans-serif"
    fontSize: "3.5rem"
    fontWeight: "700"
    lineHeight: "1.1"
    letterSpacing: "-0.02em"
  headline-md:
    fontFamily: "Public Sans, sans-serif"
    fontSize: "1.75rem"
    fontWeight: "600"
    lineHeight: "1.25"
  body-md:
    fontFamily: "Public Sans, sans-serif"
    fontSize: "1rem"
    fontWeight: "400"
    lineHeight: "1.5"
  label-caps:
    fontFamily: "Space Grotesk, sans-serif"
    fontSize: "0.75rem"
    fontWeight: "600"
    letterSpacing: "0.05em"
rounded:
  sm: "4px"
  md: "8px"
  lg: "16px"
  full: "9999px"
spacing:
  unit: "8px"
  sm: "8px"
  md: "16px"
  lg: "24px"
  xl: "32px"
  container-padding: "24px"
components:
  button-primary:
    backgroundColor: "var(--color-tertiary)"
    textColor: "#FFFFFF"
    borderRadius: "var(--rounded-md)"
    padding: "12px 24px"
---
```

---

## 3. Fórmulas Matemáticas de Accesibilidad WCAG 2.1

### A. Luminancia Relativa ($L$)
Para un color sRGB normalizado en $[0, 1]$:
$$c_{\text{linear}} = \begin{cases} \frac{c}{12.92} & \text{si } c \le 0.04045 \\ \left(\frac{c + 0.055}{1.055}\right)^{2.4} & \text{si } c > 0.04045 \end{cases}$$

$$L = 0.2126 \cdot R_{\text{linear}} + 0.7152 \cdot G_{\text{linear}} + 0.0722 \cdot B_{\text{linear}}$$

### B. Ratio de Contraste ($CR$)
Dadas las luminancias de dos colores $L_1$ (más claro) y $L_2$ (más oscuro):
$$CR = \frac{L_1 + 0.05}{L_2 + 0.05}$$

* **WCAG AA:** $CR \ge 4.5:1$ (texto estándar) y $CR \ge 3.0:1$ (texto grande $\ge 18\text{pt}$ o componentes interactivos).
* **WCAG AAA:** $CR \ge 7.0:1$ (texto estándar) y $CR \ge 4.5:1$ (texto grande).

---

## 4. Integración Automática con CSS Variables & Tailwind

Cualquier archivo `DESIGN.md` es transpilable directamente a tokens CSS nativos:

```css
:root {
  /* Colors */
  --color-primary: #1A1C1E;
  --color-tertiary: #B8422E;
  --color-neutral: #F7F5F2;
  --color-surface: #FFFFFF;
  
  /* Typography */
  --font-family-display: 'Public Sans', sans-serif;
  --font-size-display-lg: 3.5rem;
  --line-height-display-lg: 1.1;
  
  /* Radii & Spacing */
  --rounded-md: 8px;
  --spacing-md: 16px;
}
```
