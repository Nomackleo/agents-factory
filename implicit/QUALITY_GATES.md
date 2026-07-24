# Quality Gates & Compliance Metrics (NIST CSF 2.0, ISO 42001 & ISO 27001)

Este documento establece las barreras de aceptación universales para todos los componentes (prompts, código, esquemas XML/JSON) generados por los agentes dentro de la Fábrica.

---

## 1. Criterios de Rendimiento y Resiliencia Digital (DORA Metrics)

El pipeline de generación y los ecosistemas resultantes serán evaluados bajo:

- **Deployment Frequency (Frecuencia de Despliegue):** La arquitectura de subagentes y la paralelización de tareas (Gatherer -> Architect -> Builder) debe entregar stacks completos en tiempo mínimo sin intervención manual.
- **Lead Time for Changes:** Re-generación ágil de flujos y skills Neo-CRISPE sin pérdida de contexto.
- **Change Failure Rate (Tasa de Fallos):** Reducción de fallos mediante TDD (Test-Driven Development) y el validador estricto `bin/handoff-validator.py` antes de escribir en disco.
- **Time to Restore Service (MTTR < 60s):** En caso de errores de formato JSON/XML o fallos de API, el agente Supervisor debe aplicar *fallback* automático a `gemini-3.6-flash` o `gemini-3.5-flash` para autorreparar la ejecución.

---

## 2. Eficiencia y Gobernanza de IA (ISO 42001 AIMS & SPACE Framework)

- **AIMS Clause 8.2 (Transparencia y Esquemas XML):** Todo handoff entre subagentes requiere la envoltura XML explícita (`<corporate_context>`, `<reasoning_trace>`, `<schema>`). Se prohíbe el paso de texto plano ambiguo.
- **AIMS Clause 8.4 (Control Humano y Sandbox):** NINGÚN agente puede volcar código o skills a producción o a la memoria permanente sin la validación Human-in-the-Loop (HITL). Las salidas de `/learn` se escriben EXCLUSIVAMENTE en `.agents/skills/staging/`.
- **Rendimiento Algorítmico y Token Economy:** Optimización innegociable de consumo de contexto. La navegación del código se realiza vía `Codebase-Memory-MCP` (SQLite) y resúmenes focalizados.

---

## 3. Barreras de Ciberseguridad (NIST CSF 2.0 & ISO 27001 ISMS)

- **NIST CSF PR.DS-01 & ISO 27001 ISMS-DP-02 (Filtrado de Secretos):** Bloqueo automático en el hook `PreToolUse` de cualquier argumento o payload que contenga API Keys, tokens OAuth, JWTs o credenciales en texto plano.
- **NIST CSF DE.AE-01 (Detección de Prompt Injection):** Sanitización obligatoria en `PostToolUse` de cualquier contenido externo obtenido via web search o scraping antes de inyectarse al contexto activo.
- **NIST CSF PR.PS-01 (Ejecución Aislada):** Limitación estricta de escrituras físicas al directorio de la fábrica `agents-factory/`, el de proyectos `projects/`, o la carpeta temporal `scratch/`.
- **NIST CSF RS.MA-01 (Dead-man Switch):** Aborto automático de la tarea si un subagente excede `max_turns` o entra en bucles recursivos.
