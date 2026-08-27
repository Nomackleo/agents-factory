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

## 3. Playbooks de Estilo Audiovisual (*Style Playbooks*)

1. **`premium-minimalist`:** Fondos oscuros profundos (`#0A0A0C`), tipografía Geist / Inter, transiciones nítidas y gráficos de líneas ultrafinas.
2. **`anime-ghibli`:** Paleta pictórica suave, texturas orgánicas, iluminación dorada crepuscular y ritmos visuales pausados.
3. **`flat-motion-graphics`:** Colores saturados de alto contraste, formas geométricas audaces y cinética elástica para explicaciones técnicas.
4. **`clean-professional`:** Colores corporativos confiables (azul pizarra, blanco níveo), tarjetas estructuradas y ritmo constante.

---

## 4. Estándares de Accesibilidad Audiovisual (WCAG 2.1 AA / EBU R128)

- **Subtítulos Quemados:** Fuente sans con borde de alto contraste (`text-shadow: 0 2px 8px rgba(0,0,0,0.8)` o caja opaca al 80%).
- **Normalización de Audio:** Pista de voz fijada a $-16 \text{ LUFS}$ (estéreo online) / $-23 \text{ LUFS}$ (broadcast) con margen de pico real de $-1.0 \text{ dBTP}$.
- **Música de Fondo (Ducking):** Reducción automática de $-14 \text{ dB}$ a $-18 \text{ dB}$ durante la presencia de voz en off.
