# Las 5 Capas de Arquitectura de la Fábrica y Modelo Defensivo en 3 Capas (NIST CSF 2.0 & ISO 42001 Alignment)

Todo ecosistema generado o ejecutado dentro de la Fábrica de Antigravity debe estructurarse y validarse a través de estas cinco capas fundamentales y el marco defensivo en tres niveles para garantizar seguridad (Zero Trust), determinismo y resiliencia digital (DORA).

---

## 1. Capas Fundamentales de la Arquitectura

### 1. Capa de Identidad (NIST CSF GV.OC & ISO 42001 Clause 6.1)

Define de manera unívoca el "Quién" (Roles estrictos en Neo-CRISPE). Cada subagente debe poseer una firma (`SKILL.md`) con un propósito inmutable. El modelo no debe asumir roles múltiples que crucen dominios.

### 2. Capa de Entrada / Ingesta (NIST CSF PR.DS & ISO 27001 ISMS-DP-02)

Define el "Qué" y valida la pureza del contexto. Sanitización de documentos/web en `<external_data>`, filtrado de secretos en `PreToolUse` y prevención de prompt injection.

### 3. Capa de Ejecución (NIST CSF PR.PS & ISO 42001 Clause 8.4)

Define el "Dónde" y "Cómo" bajo estricto aislamiento. Sandboxing en `agents-factory/`, `projects/` o `scratch/`. Validación de conexiones salientes e intercepción de herramientas.

### 4. Capa de Control (NIST CSF RS.MA & DORA MTTR)

Mecanismos preventivos y reactivos (Ask, Allow, Deny) y Dead-man Switch sobre la base de datos relacional SQLite (`Codebase-Memory-MCP`).

### 5. Capa de Observabilidad & Aprendizaje (NIST CSF RC.CO & ISO 42001 Clause 8.2)

Trazabilidad XML determinista y consolidación de aprendizaje en `.agents/skills/staging/`.

---

## 2. Marco Defensivo de Seguridad Extra (Defense-in-Depth)

1. **Capa de Conversación (Boundary Security):** Sanitización de contexto externo en `<external_data>`, detección determinista de Prompt Injection (directa/indirecta) y Token Budgeting por nivel de esfuerzo (Low, Medium, High, Max).
2. **Capa de Aplicación (Subagent & State Security):** Validación de contrato Handoff JSON (`bin/handoff-validator.py`), intercepción Sandbox Pre-Tool (`hooks/pre-tool-validation.json`) y aislamiento de roles Neo-CRISPE.
3. **Capa de Infraestructura (Persistence & Key Vault):** Modelo de Responsabilidad Compartida (*Shared Responsibility Model*), aislamiento estricto de entregables en `projects/`, memoria relacional SQLite desacoplada por proyecto y Zero Hardcoding de credenciales.
