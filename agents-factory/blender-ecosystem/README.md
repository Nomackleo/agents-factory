# Blender Ecosystem (VFX & 3D Automation)

**WHO**: Operado por los equipos de Arte Técnico y Automatización 3D.
**WHAT**: Este ecosistema gestiona y automatiza flujos de trabajo en Blender 3D (Renderizado, Topología, Procedural, Shading) mediante el uso de la API Python (`bpy`).
**WHEN**: Se utiliza para tareas de generación de activos, iluminación automatizada e integración de pipelines de render continuo (CI/CD para 3D).
**WHERE**: Dominio exclusivo `agents-factory/blender-ecosystem/`.
**WHY**: Eliminar tareas repetitivas en la línea de ensamble de VFX y garantizar precisión topológica y de sombreado mediante código determinista, bajo estándares estrictos ISO y DORA.

## Topología del Ecosistema

```mermaid
graph TD
    A[Blender Ecosystem] --> B(.agents/skills/)
    A --> C(.agents/workflows/)
    A --> D(.agents/rules/)
    A --> E(brain/)
    A --> F(knowledge/)

    B --> B1[00-supervisor-router]
    B --> B2[01-research-gatherer]
    B --> B3[02-workflow-architect]
    B --> B4[03-builders]
    
    B4 --> B4_1(topology-agent)
    B4 --> B4_2(shading-agent)
    B4 --> B4_3(lighting-agent)

    classDef domain fill:#1E293B,stroke:#3B82F6,stroke-width:2px,color:#F8FAFC
    classDef agent fill:#0F172A,stroke:#10B981,stroke-width:1px,color:#E2E8F0
    class A,B,C,D,E,F domain
    class B1,B2,B3,B4,B4_1,B4_2,B4_3 agent
```
