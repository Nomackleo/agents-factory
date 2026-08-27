# Reglas Operacionales del Ecosistema OpenMontage

**Alcance:** Todos los pipelines, directores de etapa, runtimes de renderizado y generadores de activos en OpenMontage  
**Cumplimiento:** ISO 9001:2015, ISO 42001 (AIMS), WCAG 2.1 AA/AAA.

---

## 1. Validación Estricta de Artefactos Canónicos

1. Ningún agente puede avanzar a la siguiente etapa del pipeline sin haber emitido y validado su artefacto canónico JSON contra su esquema formal en `schemas/artifacts/`:
   - `brief.json` ➔ validado por `brief.schema.json`
   - `script.json` ➔ validado por `script.schema.json`
   - `scene_plan.json` ➔ validado por `scene_plan.schema.json`
   - `asset_manifest.json` ➔ validado por `asset_manifest.schema.json`
   - `edit_decisions.json` ➔ validado por `edit_decisions.schema.json`
   - `render_report.json` ➔ validado por `render_report.schema.json`
   - `publish_log.json` ➔ validado por `publish_log.schema.json`

---

## 2. Puertas de Aprobación Humana (HITL Gates)

1. Antes de iniciar renderizados pesados o generaciones costosas de video por IA (Kling, Wan, Runway, Fal.ai), el agente debe:
   - Presentar el plan de escenas (`scene_plan.json`) y el presupuesto estimado en USD.
   - Detenerse y esperar confirmación explícita del usuario (*Human-in-the-Loop*).

---

## 3. Gobernanza de Audio y Accesibilidad

1. Todo video final debe incorporar subtitulación sincronizada (mediante WhisperX o transcripción de guion) y cumplir con el contraste mínimo de WCAG 2.1 AA.
2. Los niveles de audio deben normalizarse obligatoriamente a $-16 \text{ LUFS}$ para plataformas digitales con ducking automático de música de fondo.
