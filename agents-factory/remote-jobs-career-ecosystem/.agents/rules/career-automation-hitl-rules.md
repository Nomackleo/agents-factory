# Reglas Operativas y Protocolo HITL: Remote Jobs & Reactive Resume Ecosystem

**Propósito:** Definir los principios inmutables para la ingesta de ofertas laborales remotas, generación reactiva de currículums hiperpersonalizados, redacción de cartas de presentación y control estricto *Human-in-the-Loop* (HITL).  
**Cumplimiento Normativo:** ISO 9001:2015 (Calidad de Procesos), ISO 27001 (Privacidad de Datos y Confidencialidad), ISO 42001 (AIMS).

---

## 1. Principio Inmutable de Human-in-the-Loop (HITL Obligatorio)

1. **Cero Postulación Automática a Ciegas:**
   - Queda **estrictamente prohibido** enviar candidaturas o correos a reclutadores sin la revisión y aprobación explícita de Leonel (HITL).
   - El sistema debe generar el dossier completo de postulación (CV personalizado + Carta de presentación + Análisis de compatibilidad ATS) y presentarlo para validación humana.
2. **Veracidad Absoluta (Cero Alucinación de Experiencia):**
   - Todo logro, métrica, tecnología y certificación incluida en los currículums debe derivar estrictamente del perfil maestro verificado (`knowledge/nomack_executive_master_profile.md`).
   - Prohibido inventar empresas, títulos o métricas inexistentes.

---

## 2. Reglas de Ingeniería de Currículum y Optimización ATS

1. **Compatibilidad ATS (Applicant Tracking Systems):**
   - Estructura limpia y jerárquica sin tablas anidadas complejas, gráficos no legibles por OCR ni columnas múltiples que confundan a parsers (Greenhouse, Lever, Workable, Taleo).
   - Inclusión natural de palabras clave técnicas exigidas en la oferta de trabajo (*Keyword Density* óptima entre $3\%$ y $5\%$).
2. **Metodología STAR / Google XYZ para Viñetas:**
   - Cada logro debe redactarse bajo la fórmula: *"Logré [X], medido por [Y], haciendo [Z]"* (ej. *"Reduje la latencia de inferencia en un 40% (Y) implementando Compute Shaders en WebGPU (Z) para la arquitectura de animación neuronal (X)"*).
3. **Extensión Estricta:**
   - Máximo 1 o 2 páginas según el nivel de seniority y relevancia directa para el rol.

---

## 3. Gobernanza del Pipeline y Registro en Workspace

1. **Trazabilidad en Google Sheets:**
   - Toda oportunidad analizada debe registrarse en la hoja de cálculo del pipeline (`google-workspace-ecosystem`) con: Empresa, Rol, URL de la oferta, Puntuación de afinidad (Score $0-100\%$), Estado (Evaluado, Aprobado HITL, Postulado, Entrevista, Oferta) y Fecha.
