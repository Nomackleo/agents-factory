# Las 5 Capas de Arquitectura de la Fábrica (NIST CSF 2.0 & ISO 42001 Alignment)

Todo ecosistema generado o ejecutado dentro de la Fábrica de Antigravity debe estructurarse y validarse a través de estas cinco capas fundamentales para garantizar seguridad (Zero Trust), determinismo y resiliencia digital (DORA).

---

## 1. Capa de Identidad (NIST CSF GV.OC & ISO 42001 Clause 6.1)

Define de manera unívoca el "Quién" (Roles estrictos en Neo-CRISPE). Cada subagente debe poseer una firma (`SKILL.md`) con un propósito inmutable. El modelo no debe asumir roles múltiples que crucen dominios (ej. un auditor de código no puede compilar y ejecutar simultáneamente).

---

## 2. Capa de Entrada / Ingesta (NIST CSF PR.DS & ISO 27001 ISMS-DP-02)

Define el "Qué" y valida la pureza del contexto.

- **Sanitización Obligatoria:** Todo documento externo, fragmento de código o resultado web pasa por el `04-security-sanitizer` en `PostToolUse`.
- **Filtrado de Secretos:** Escaneo automático de tokens, API keys y credenciales en `PreToolUse`.
- **Prevención de Inyecciones (NIST DE.AE-01):** Se bloquean y escanean activamente textos ofuscados (Base64, Unicode oculto) e intentos de redirección de datos.

---

## 3. Capa de Ejecución (NIST CSF PR.PS & ISO 42001 Clause 8.4)

Define el "Dónde" y "Cómo" bajo estricto aislamiento.

- **Sandboxing:** Todo código generado o ejecutado debe limitarse a `agents-factory/`, `projects/` o `scratch/`.
- **Validación de Conexiones Web (HITL):** Cualquier conexión saliente (APIs externas, GitHub, scraping) requiere confirmación del humano mediante el sistema de triaje (Ask, Allow, Deny).

---

## 4. Capa de Control (NIST CSF RS.MA & DORA MTTR)

Mecanismos preventivos y reactivos que gestionan la soberanía humana sobre el loop algorítmico.

- **Sistema de Triaje (Ask, Allow, Deny):** Todo requerimiento de permisos exige aprobación explícita.
- **Dead-man Switch (NIST RS.MA-01):** Si un agente entra en bucle o excede `max_turns`, el switch aborta la operación, restituyendo el estado desde la base relacional SQLite (`Codebase-Memory-MCP`).

---

## 5. Capa de Observabilidad & Aprendizaje (NIST CSF RC.CO & ISO 42001 Clause 8.2)

- **Trazabilidad XML Determinista:** Cada salto entre capas deja rastro en el contrato `<corporate_context>` XML.
- **Aprendizaje Continuo (Stop Hook `/learn`):** Toda solución exitosa se destila y consolida EXCLUSIVAMENTE en `.agents/skills/staging/` dentro del workspace.
