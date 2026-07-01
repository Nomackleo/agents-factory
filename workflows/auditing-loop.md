# Workflow: Auditing Loop (Agentic SDK Framework)

El ecosistema opera bajo un ciclo determinista de auditoría inspirado en la arquitectura canónica de agentes de Claude (Agent SDK Loop). Este *loop* gestiona el ciclo de vida de los mensajes, la ejecución paralela y secuencial de herramientas, los niveles de esfuerzo computacional y el límite del *context window* para garantizar una iteración (Test - Eval - Monitor - Iterate) estricta y sin alucinaciones.

## 1. Test (Context & Tool Execution)
En esta fase, iniciamos el *Turn-Based Execution*.
- **Message Lifecycle (Init):** El Supervisor inicializa el pipeline emitiendo un `SystemMessage` de enrutamiento.
- **Delegación al Research Gatherer:** Se asigna un nivel de razonamiento `effort: low` o `effort: medium`. Su único propósito es extraer "Ground Truth" externa e interna.
- **Parallel Tool Execution:** Las herramientas de solo-lectura (`Read`, `Glob`, `Grep`, `WebSearch`) se ejecutan de manera concurrente para minimizar la latencia.
- **Feedback Loop:** Las herramientas retornan `UserMessage` con los resultados. El Supervisor evalúa la validez de los datos (e.g., URLs reales, APIs válidas).

## 2. Evaluation (Architectural Reasoning)
El sistema avanza al diseño del *Blueprint*, requiriendo máxima profundidad de análisis.
- **Deep Reasoning (Effort: Max):** El `02-workflow-architect` se invoca con `effort: max` (Extended Thinking habilitado si aplica).
- **Handoff (AssistantMessage):** El arquitecto estructura un `<architect_blueprint>`.
- **Quality Gate Validation:** El Supervisor evalúa el blueprint contra los `QUALITY_GATES.md` y `rules/security-and-compliance.md`. Si se detecta una violación, se emite un `UserMessage` de fallo (Error Feedback) y el loop se reinicia (Turno +1).

## 3. Monitoring (Sequential Execution & Budgeting)
Inicia la escritura de la arquitectura generada, requiriendo operaciones de estado.
- **Sequential Tool Execution:** El `03-crispe-generator` invoca herramientas que modifican el estado (`Edit`, `Write`, `Bash`). Estas se ejecutan de forma **estrictamente secuencial** para evitar condiciones de carrera o conflictos de *filesytem*.
- **Pre-Tool Validation (Hooks):** Todo intento de escritura dispara un validador que intercepta herramientas fuera del dominio `agents-factory/`.
- **Limits & Thresholds:** El Supervisor impone un `max_turns` y un `max_budget` para evitar loops infinitos (Infinite Iteration Traps). Si se alcanza el umbral de coste o turnos sin éxito, el sistema emite un error estructurado y se detiene (abortando con `ResultMessage` tipo `error_max_turns`).

## 4. Iteration (Result Handling & Compaction)
Fase final del turno.
- **Context Window Management (Compaction):** Si el contexto crece por encima de umbrales críticos, se fuerza una compresión del estado (Automatic Compaction). El Supervisor resume la sesión en `brain/sessions/` y emite un `compact_boundary` (vaciando el buffer de mensajes redundantes).
- **Final Result:** Una vez completada la generación, el Supervisor detiene las llamadas a herramientas y retorna un texto limpio y declarativo.
- **ResultMessage:** El pipeline devuelve el control al sistema origen, exportando métricas de éxito (`subtype: success`), recuento de tokens (DORA economics) y el coste incurrido en el ciclo.

> **Regla Crítica:** Un *Turno* no termina hasta que el resultado de la herramienta regresa al modelo. El *Loop* global no termina hasta que el Supervisor decide que no requiere más llamadas a herramientas. Todo esto corre de forma asíncrona sin intervención humana hasta tocar los `max_turns` o un Checkpoint (HITL).
