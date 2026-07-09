# Business Diagnostic Ecosystem

**WHAT**: Este ecosistema se encarga del Diagnóstico de Negocio (BDI - Business Diagnostic Intelligence), utilizando metodologías científicas (McKinsey 7S, COBIT 2019, PuMP, APQC PCF, TOGAF ACMM) y escalas conductuales ancladas (BARS). Consolida toda la información en un Documento Corporativo Maestro con el contrato de datos XML `<corporate_context>`.

## Ecosystem Routing (Graphify Core)

1. `mckinsey-7s-evaluator`: Diagnostica la alineación estratégica, cultural y organizacional.
2. `process-capability-assessor`: Evalúa la madurez y estabilidad de procesos.
3. `it-architecture-auditor`: Diagnostica la deuda técnica y arquitectura de TI.
4. `corporate-master-compiler`: Compila y genera el Documento Corporativo Maestro unificado.

> [!IMPORTANT]
> A partir de la versión 2.5 del *Core*, este ecosistema se vincula directamente a la **Fase 1 (Search)** del *Iterative Retrieval Pattern* del `00-supervisor-router`. Se utiliza para realizar un levantamiento estricto de requerimientos y *Ground Truth* antes de permitir que otros agentes diseñen la solución.

## Tubería de Diagnóstico BDI (Graphify Map)

```mermaid
graph TD
    User([Usuario / CEO]) --> |Solicita Diagnóstico| Router{Routing Matrix}
    Router --> |Estrategia/Cultura| A1[.agents/skills/mckinsey-7s-evaluator]
    Router --> |Procesos/Madurez| A2[.agents/skills/process-capability-assessor]
    Router --> |Tecnología/IT| A3[.agents/skills/it-architecture-auditor]
    
    A1 --> C[.agents/skills/corporate-master-compiler]
    A2 --> C
    A3 --> C
    
    C --> Output[/Documento Corporativo Maestro con corporate_context XML/]
```
