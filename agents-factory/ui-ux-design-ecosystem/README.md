# UI/UX Design Ecosystem

**WHAT**: Este ecosistema gestiona toda la capa de diseño, experiencia de usuario (UX) y validación de accesibilidad (Ergonomía y Normativas WCAG/ISO 9241). Es el responsable de generar los sistemas de diseño, wireframes y prototipos a partir de los requerimientos, para luego ser consumidos por el ecosistema de ingeniería de software.

## Ecosystem Routing (Graphify Core)

El ecosistema opera mediante tres sub-gremios hiper-especializados:

1. **Design System Guild**: Crea la identidad visual y los tokens.
   - `.agents/skills/design-tokens-architect`
   - `.agents/skills/figma-stitch-integrator`
2. **UX Guild**: Diseña flujos, arquitecturas de la información e interacciones visuales avanzadas.
   - `.agents/skills/ux-flow-designer`
   - `.agents/skills/micro-interactions-animator`
3. **Ergonomics & Accessibility Guild**: Audita el diseño asegurando accesibilidad estricta.
   - `.agents/skills/wcag-accessibility-auditor`
   - `.agents/skills/screen-reader-testing-expert`

> [!IMPORTANT]
> **Flexibilidad Semántica Híbrida:** Los gremios de diseño (Tokens y UX) operan con **creatividad paramétrica** (Top-P relajado) para maximizar la innovación y calidad estética. Sin embargo, el Gremio de Accesibilidad opera con **rigor absoluto (Temperatura 0)**. Toda conexión de red a Figma u otras herramientas dispara la **Capa de Control (Triaje HITL)**.

## Architectural Topology (Graphify Map)

```mermaid
graph TD
    Input[/Requerimientos y Docs-as-Code/] --> Router{Routing Matrix}
    
    Router --> DSG[Design System Guild]
    Router --> UXG[UX Guild]
    
    DSG --> |Tokens & CSS Variables| UXG
    UXG --> |Flujos UI & Animaciones| EAG[Ergonomics & Accessibility Guild]
    
    EAG --> Output[/Tokens y Flujos Listos para Software Eng/]
```
