# Workflow: Auditing Loop (Agentic SDK Framework)

El ecosistema opera bajo un ciclo determinista de auditoría inspirado en la arquitectura canónica de agentes de Claude (Agent SDK Loop). Este *loop* gestiona el ciclo de vida de los mensajes, la ejecución paralela y secuencial de herramientas, los niveles de esfuerzo computacional y el límite del *context window* para garantizar una iteración (Test - Eval - Monitor - Iterate) estricta y sin alucinaciones.

## Fase 1: Búsqueda (Search) e Ingesta
En esta fase, iniciamos el *Turn-Based Execution* aplicando la **Capa de Entrada**.
- **Message Lifecycle (Init):** El Supervisor inicializa el pipeline emitiendo un `SystemMessage` de enrutamiento.
- **Ingesta y Sanitización (`04-security-sanitizer`):** Antes de cualquier lectura, el Sanitizador evalúa los archivos del repositorio o input del humano buscando código oculto (Base64, HTML) y previene inyecciones. Si encuentra anomalías (ej. redirección de correos), lanza un **ASK (Triaje)** al humano.
- **Levantamiento de Requerimientos (Business Diagnostic):** Especialmente alineado con el `business-diagnostic-ecosystem`, se extrae el contexto necesario (Ground Truth) para garantizar alta calidad, granularidad y economía.
- **Delegación al Research Gatherer:** Se asigna un nivel de razonamiento `effort: low` o `medium`.
- **Parallel Tool Execution:** Herramientas de solo-lectura se ejecutan de manera concurrente.

## Fase 2: Ejecución (Execution) y Razonamiento
El sistema avanza al diseño del *Blueprint* y la construcción de la **Capa de Ejecución**.
- **Deep Reasoning (Effort: Max):** El `02-workflow-architect` se invoca con `effort: max`. (Nota: en entornos como `software-engineering`, se permite creatividad paramétrica para evitar bucles de depuración ciegos).
- **Sequential Tool Execution:** El `03-crispe-generator` y los *Builders* invocan herramientas que modifican el estado.
- **Handoff & Pre-Tool Validation (Hooks):** El Supervisor evalúa el blueprint. Cualquier intento de ejecución web o de bash que exceda el Sandboxing dispara el Triaje (ASK/ALLOW/DENY). Si se detecta violación grave, se activa el **Dead-man switch**.

## Fase 3: Auditoría (Audit) y Monitoreo
Fase final del ciclo (Test - Eval - Monitor - Iterate).
- **Quality Gate Validation:** Se audita el código generado contra los `QUALITY_GATES.md` (ISO/SOC2/DORA).

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
