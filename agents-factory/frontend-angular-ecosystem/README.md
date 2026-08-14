# Frontend Angular Ecosystem (Official Angular Agent Skills)

**WHO**: Operado por los equipos de Ingeniería Web Frontend y Arquitectura Angular.
**WHAT**: Este ecosistema integra las habilidades de agente oficiales de Angular (`angular-developer` y `angular-new-app`) publicadas por el equipo central de Angular en Google LLC (`https://github.com/angular/skills`).
**WHEN**: Se utiliza para el desarrollo de componentes modernos de Angular v22+, reactividad con Signals (`signal`, `computed`, `linkedSignal`, `resource`, `httpResource`), formulación con Signals Forms, inyección con `inject()`, enrutamiento SSR e integración con el servidor MCP de Angular CLI.
**WHERE**: Dominio exclusivo `agents-factory/frontend-angular-ecosystem/`.
**WHY**: Eliminar patrones obsoletos (`NgModules`, inyección por constructor, `*ngIf`) y garantizar que todo el código frontend Angular sea moderno, declarativo, libre de errores y verificado mediante `ng build`.

## Topología del Ecosistema

```mermaid
graph TD
    A[Frontend Angular Ecosystem] --> B(.agents/skills/)
    A --> C(README.md)

    B --> B1[angular-developer]
    B --> B2[angular-new-app]

    B1 --> B1_1(Signals & Reactivity)
    B1 --> B1_2(Control Flow @if @for)
    B1 --> B1_3(Dependency Injection inject)
    B1 --> B1_4(Signals Forms)
    B1 --> B1_5(Angular MCP & CLI)

    classDef domain fill:#1E293B,stroke:#DD0031,stroke-width:2px,color:#F8FAFC
    classDef agent fill:#0F172A,stroke:#C3002F,stroke-width:1px,color:#E2E8F0
    class A,B,C domain
    class B1,B2,B1_1,B1_2,B1_3,B1_4,B1_5 agent
```
