# Archify Diagrams & Visual Architecture Ecosystem — Universal Antigravity Architecture

**Autoría Oficial:** Antigravity AI & Archify Framework (`tt-a1i/archify`)  
**WHAT:** Ecosistema Agéntico de Generación, Compilación y Renderizado de **Diagramas de Arquitectura, Flujo de Datos, Secuencias, Ciclos de Vida y Workflows** mediante especificaciones JSON IR fuertemente tipadas, compiladas a entregables HTML/SVG autocontenidos e interactivos con soporte de *Taste Skill* (Tipografía Suiza, Modo Presentación Fullscreen, selector de tema Dark/Light y trazado de rutas de ejecución).  
**División Corporativa:** `03_creative_production_and_3d` (Creative Suite, 3D Engineering & Digital Media).  
**Cumplimiento Normativo:** TOGAF 10 (Arquitectura Empresarial), ISO 25010 (Calidad de Software), ISO 9001:2015 (Documentación Técnica Verificable).

---

## 1. Topología del Ecosistema Agéntico (Graphify Map)

```mermaid
graph TD
    %% Entradas
    Input[/Descripción de Arquitectura / Código / Requerimientos de Sistema/] --> Router{Archify Orchestrator}

    %% Subagentes Especialistas
    subgraph Guilds["Gremios Especialistas en Visual Architecture & Archify"]
        G1[archify-ir-compiler-architect<br/>Compilación Typed JSON IR + Boundaries + Routes]
        G2[archify-taste-html-designer<br/>Taste Skill + Presentaciones HTML Fullscreen + Dark/Light]
        G3[archify-workspace-topology-mapper<br/>Topologías Google Workspace + IAM + RAG NotebookLM]
    end

    Router --> Guilds

    %% Cohesión Transversal
    subgraph Transversal["Cohesión Transversal con Ecosistemas Antigravity"]
        UIUX["ui-ux-design-ecosystem<br/>(Tokens de diseño, tipografía suiza, estética de lujo)"]
        WORKSPACE["google-workspace-ecosystem<br/>(Diagramación de Shared Drives, flujos de correo y GA4)"]
        SOFTWARE["software-engineering-ecosystem<br/>(Diagramas C4, microservicios y pasarelas API)"]
        DOCS["docs-as-code-executive-ecosystem<br/>(Memorandos ejecutivos e informes periciales)"]
        SECURITY["cybersecurity-ecosystem<br/>(Perímetros de seguridad, IAM y Model Armor)"]
    end

    Guilds <--> Transversal
```

---

## 2. Catálogo de Subagentes Especialistas (Neo-CRISPE v2.0)

| Subagente | Responsabilidad Principal | Herramientas & Ámbitos |
| :--- | :--- | :--- |
| **[`archify-ir-compiler-architect`](file:///c:/Users/Nomack/Documents/workspace/agents/antigravity/dev/prompt-generator/agents-factory/archify-diagrams-ecosystem/.agents/skills/archify-ir-compiler-architect/SKILL.md)** | Modelado topológico y compilación determinista de especificaciones JSON IR (Architecture, Data-Flow, Sequence, Lifecycle, Workflow). | `archify.compiler`<br>`json_ir.validator` |
| **[`archify-taste-html-designer`](file:///c:/Users/Nomack/Documents/workspace/agents/antigravity/dev/prompt-generator/agents-factory/archify-diagrams-ecosystem/.agents/skills/archify-taste-html-designer/SKILL.md)** | Integración de diagramas interactivos en presentaciones HTML de alta gama con Taste Skill (Diseño Suizo, Fullscreen, Dark/Light, Share Cards). | `taste_skill.html`<br>`svg.interactive` |
| **[`archify-workspace-topology-mapper`](file:///c:/Users/Nomack/Documents/workspace/agents/antigravity/dev/prompt-generator/agents-factory/archify-diagrams-ecosystem/.agents/skills/archify-workspace-topology-mapper/SKILL.md)** | Diagramación especializada de topologías de Google Workspace Enterprise (Shared Drives, IAM/2FA, flujos de correo, Gemini y NotebookLM). | `workspace.topology`<br>`iam.mapper` |

---

## 3. Matriz de Cohesión Transversal Soberana (Zero-Overlap Policy)

1. **`ui-ux-design-ecosystem`:** Provee el sistema de tokens de marca, fuentes tipográficas suizas y guías cromáticas; Archify compila los diagramas vectoriales interactivos.
2. **`google-workspace-ecosystem`:** Define la configuración operativa y APIs de Workspace; Archify genera la arquitectura visual interactiva y los planos de topología.
3. **`software-engineering-ecosystem`:** Define el código, APIs y arquitectura de backend; Archify produce los diagramas de C4, secuencias y ciclos de vida.
4. **`docs-as-code-executive-ecosystem`:** Incrusta los diagramas visuales en reportes ejecutivos para juntas directivas y auditorías de calidad ISO 9001.

---

## 4. Base de Conocimiento Especializada (`knowledge/`)

- [`archify_architecture_and_json_ir_mastery.md`](file:///c:/Users/Nomack/Documents/workspace/agents/antigravity/dev/prompt-generator/agents-factory/archify-diagrams-ecosystem/knowledge/archify_architecture_and_json_ir_mastery.md) ➔ Tipos de diagramas, esquema JSON IR v2 y compilación determinista.
- [`taste_skill_archify_visual_synthesis.md`](file:///c:/Users/Nomack/Documents/workspace/agents/antigravity/dev/prompt-generator/agents-factory/archify-diagrams-ecosystem/knowledge/taste_skill_archify_visual_synthesis.md) ➔ Integración con Taste Skill, tipografía suiza, atajos de teclado y fullscreen.
- [`google_workspace_topology_architecture_mastery.md`](file:///c:/Users/Nomack/Documents/workspace/agents/antigravity/dev/prompt-generator/agents-factory/archify-diagrams-ecosystem/knowledge/google_workspace_topology_architecture_mastery.md) ➔ Capas arquitectónicas de Google Workspace (IAM, Shared Drives, Gemini In-App, NotebookLM).
