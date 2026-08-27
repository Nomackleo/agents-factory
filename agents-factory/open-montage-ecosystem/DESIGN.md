# Especificación de Diseño Visual y Motion: OpenMontage Ecosystem (DESIGN.md)

**Propósito:** Definir los estándares estéticos, relaciones de aspecto, tokens de movimiento, paletas cromáticas para video y normas de accesibilidad audiovisual en el ecosistema OpenMontage.

---

## 1. Perfiles de Renderizado y Relaciones de Aspecto

| Perfil | Resolución | FPS | Relación de Aspecto | Uso Principal |
| :--- | :---: | :---: | :---: | :--- |
| **`youtube-landscape`** | $1920 \times 1080$ / $3840 \times 2160$ | 30 / 60 | 16:9 | YouTube, Masterclass, Documentales, Cine Web |
| **`reels-shorts-tiktok`** | $1080 \times 1920$ | 30 / 60 | 9:16 | Instagram Reels, TikTok, YouTube Shorts |
| **`square-social`** | $1080 \times 1080$ | 30 | 1:1 | Feed Instagram, LinkedIn, X Video |
| **`cinematic-scope`** | $3840 \times 1608$ | 24 | 2.39:1 (Anamórfico) | Teasers de Alta Gama, Publicidad Cinemática |

---

## 2. Tokens de Movimiento y Curvas de Aceleración (*Motion Tokens*)

```json
{
  "motion": {
    "subtle_transition": { "duration_ms": 200, "easing": "cubic-bezier(0.16, 1, 0.3, 1)" },
    "kinetic_emphasis": { "duration_ms": 400, "easing": "cubic-bezier(0.34, 1.56, 0.64, 1)" },
    "cinematic_pan": { "duration_ms": 1200, "easing": "cubic-bezier(0.25, 0.1, 0.25, 1.0)" },
    "spring_physics": { "stiffness": 180, "damping": 18, "mass": 1 }
  }
}
```

---

## 3. Playbooks y Familias de Estilo Audiovisual (*Style Playbooks*)

Los agentes de OpenMontage disponen de un catálogo no restringido de estéticas visuales parametrizadas en `styles/*.yaml` y documentadas en [`knowledge/artistic_styles_and_aesthetics_encyclopedia.md`](file:///c:/Users/Nomack/Documents/workspace/agents/antigravity/dev/prompt-generator/agents-factory/open-montage-ecosystem/knowledge/artistic_styles_and_aesthetics_encyclopedia.md):

### A. Internet Aesthetics, Nostalgia Digital & Core-Cultures
- **Vaporwave / Dark Vaporwave:** Nostalgia retro-digital noventera, mármol pastel, bustos clásicos y degradados cian/magenta.
- **Synthwave / Outrun:** Neón, rejillas vectoriales en perspectiva, atardeceres magenta y síntesis ochentera.
- **Cyberpunk / Solarpunk / Steampunk / Dieselpunk / Atompunk / Raypunk / Cassette Futurism:** Corrientes especulativas y retrofuturistas.
- **Glitchcore / Hyperpop / Weirdcore / Dreamcore / Liminal Spaces / Nostalgiacore:** Deconstrucción digital y sobrecarga sensorial.
- **Dark Academia / Light Academia / Cottagecore / Goblincore:** Romanticismo humanista, botánico y rural.

### B. Interfaces, Sistemas de Diseño & Movimientos UI
- **Frutiger Aero (2004–2013) / Frutiger Eco / Frutiger Aurora:** Texturas de agua, cielos luminosos, burbujas y eskeuomorfismo amable.
- **Neo-Brutalism / Swiss Style / Bauhaus:** Bordes sólidos negros de 3px, sombras paralelas duras y tipografía de alto impacto.
- **Glassmorphism / Claymorphism / Neumorphism:** Superficies translúcidas, objetos 3D inflados y relieves extruidos suaves.
- **Y2K Aesthetic / Cyber Y2K / McBling / Acid Graphics:** Metales líquidos, cromo, tipografías clubbing y maximalismo 2000s.

### C. Texturas Cinematográficas, Render & Postproducción
- **Found Footage & VHS Degraded:** Aberración cromática analógica, ruido de cabezal y cámara en mano.
- **Low-Poly Retro 3D & 90s Raytraced CGI:** Geometrías poligonales crudas con texturas pixeladas (era PS1/Saturn).
- **Thermal Imaging (Ironbow) & Etherealcore:** Mapas de calor espectrales o sobreexposición lumínica con destellos anamórficos.

---

## 4. Estándares de Accesibilidad Audiovisual (WCAG 2.1 AA / EBU R128)

- **Subtítulos Quemados:** Fuente sans con borde de alto contraste (`text-shadow: 0 2px 8px rgba(0,0,0,0.8)` o caja opaca al 80%).
- **Normalización de Audio:** Pista de voz fijada a $-16 \text{ LUFS}$ (estéreo online) / $-23 \text{ LUFS}$ (broadcast) con margen de pico real de $-1.0 \text{ dBTP}$.
- **Música de Fondo (Ducking):** Reducción automática de $-14 \text{ dB}$ a $-18 \text{ dB}$ durante la presencia de voz en off.
