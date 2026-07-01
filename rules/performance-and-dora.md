# Performance & Delivery (DORA/SPACE)

Para lograr un "Lead Time" mínimo y una máxima eficiencia en el "Flow", todos los agentes deben regirse por las siguientes normas de rendimiento.

## 1. Economía de Tokens (Token Economics)
- **Contexto Modular:** No cargues archivos completos (ej. manuales de 1000 líneas) en el prompt activo si solo necesitas una directriz específica. Utiliza `grep_search` o lee extractos acotados.
- **Compresión de Handoffs:** El `01-research-gatherer` debe comprimir su output al mínimo indispensable (viñetas ejecutables) antes de pasarlo al `02-workflow-architect`. Nada de "relleno conversacional".

## 2. DORA Metrics (Velocidad y Estabilidad)
- **Deployment Frequency:** Prioriza generar los archivos de la fábrica en bloques o "batches" paralelos cuando sea seguro. El `03-crispe-generator` debe crear el andamiaje del ecosistema en el menor número de turnos posible.
- **Change Failure Rate:** Aplica TDD (Test-Driven Development) implícito. Antes de que el Architect entregue un blueprint, debe validar mentalmente si las conexiones de red o el flujo del webhook son posibles (ej. ¿coinciden las interfaces?).

## 3. SPACE Framework (Eficiencia de Flujo)
- **Prevención de Context Rot:** En sesiones de generación largas, si el log se infla, el Supervisor debe invocar un hook (o tarea interna) para resumir los acuerdos arquitectónicos y descartar la basura heurística generada en pasos anteriores.
- **Reducción de Latencia Cognitiva:** Los prompts generados deben tener estructuras muy jerárquicas (CRISPE) para que los agentes posteriores o el LLM final los asimilen con menor gasto de atención matemática.
