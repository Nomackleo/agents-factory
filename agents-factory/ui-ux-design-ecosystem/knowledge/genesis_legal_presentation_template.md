# Génesis Legal S.A.S. — Sistema de Diseño y Guía de Plantillas de Presentación Corporativa

Este documento contiene la especificación maestra de diseño, arquitectura HTML/CSS y componentes para la generación de presentaciones ejecutivas, propuestas comerciales y entregables forenses a nombre de **Génesis Risk Forensic & Legal S.A.S.**

---

## 🎨 Paleta de Colores Corporativa (Strict Brand Palette)

```css
:root {
  /* Marca Primaria - Deep Navy Stack */
  --navy-950: #031621; /* Fondo ultra oscuro & overlays */
  --navy-900: #04202f; /* Tarjetas & contenedores */
  --navy-800: #07283d; /* MARCA PRINCIPAL · Deep Navy */
  --navy-700: #0b3752; /* Headers secundarios & hovers */
  --navy-600: #12496b; /* Resaltados radiales */
  --navy-500: #1c5e85; /* Gradientes de acento */

  /* Marca Acentos */
  --gold: #ffd231;       /* MARCA ACENTO · CTAs, KPI, números, selección */
  --green: #056c5c;      /* MARCA · Cumplimiento OK, chips positivos */
  --green-lt: #3fbfa8;   /* Resaltados de inclusión verde */
  --crimson: #ba1650;    /* MARCA · Alertas de alto riesgo, fuera de alcance */
  --crimson-lt: #f2789e; /* Alertas texto ligero */

  /* Superficies y Reglas */
  --paper: #eef1f3;      /* Fondo claro de diapositiva */
  --paper-2: #dee4e8;    /* Contenedor claro */
  --rule: #cccccc;       /* MARCA · Gris claro para divisores */

  /* Tipografía Ink Stack */
  --ink: #f2f6f8;        /* Texto principal sobre oscuro */
  --ink-2: #a8bcc9;      /* Texto de bajada (Contrast ratio 7.76:1) */
  --ink-3: #8aa2b2;      /* Metadatos y etiquetas (Contrast ratio 5.72:1) */
}
```

---

## ✒️ Tipografía y Jerarquía Visual

| Rol | Familia Tipográfica | Pesos / Variantes | Ejemplo de Uso |
| :--- | :--- | :--- | :--- |
| **Headings / Display** | `Archivo` | 400 - 900, Stretch 88%-106% | H1, H2, H3, H4, Números KPI, Marca |
| **Editorial Body** | `Spectral` | 300 Light, 400 Regular, 600 SemiBold | Párrafos, Lead text, Citas, Entregables |
| **Data / Technical Mono**| `Chivo Mono` | 300, 400, 500, Tabular Nums | Eyebrows, Chips, Metadatos, Tablas, Tabular Nums |

---

## 🛠️ Estructura HTML de la Plantilla de Diapositivas (Deck System)

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Génesis Legal · Titulo de la Presentación</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@75..125,400..900&family=Spectral:ital,wght@0,300;0,400;0,600;1,300&family=Chivo+Mono:wght@300;400;500&display=swap" rel="stylesheet">
</head>
<body class="deck">
  <!-- Topbar Fija -->
  <header class="topbar">
    <div class="brand">
      <div class="brand__tx">
        <span class="brand__n">GÉNESIS</span>
        <span class="brand__s">RISK FORENSIC &amp; LEGAL</span>
      </div>
    </div>
    <div class="tools">
      <button class="btn" id="btn-mode">MODO PRESENTACIÓN (F)</button>
    </div>
  </header>

  <!-- Track de Diapositivas -->
  <div id="deck">
    <main id="track">
      <!-- Diapositiva 0: Portada -->
      <section class="slide" id="s0">
        <div class="hero">
          <div class="eyebrow">PROPUESTA TÉCNICA Y COMERCIAL</div>
          <h1>
            <span class="thin">AUDITORÍA INTEGRAL &amp;</span>
            <span class="gold">PERITAJE FORENSE</span>
          </h1>
          <p class="lead">Análisis multidisciplinario de riesgo, infraestructura y gobernanza digital.</p>
        </div>
      </section>
      <!-- Diapositivas adicionales... -->
    </main>
  </div>

  <!-- Barra de Navegación de Deck -->
  <footer class="deckbar">
    <div class="t">GÉNESIS · PROPUESTA TÉCNICA</div>
    <div class="c"><span id="c-curr">01</span> / <span id="c-tot">12</span></div>
  </footer>
</body>
</html>
```

---

## ⌨️ Modo Presentación y Teclas de Navegación

* **Tecla `F` o botón `MODO PRESENTACIÓN`:** Alterna entre vista de desplazamiento continuo y vista de diapositivas en pantalla completa (Fullscreen Deck).
* **Teclas `ArrowRight` / `Space`:** Avanzar a la siguiente diapositiva.
* **Teclas `ArrowLeft`:** Retroceder a la diapositiva anterior.
* **Teclas `Home` / `End`:** Ir a la primera / última diapositiva.
