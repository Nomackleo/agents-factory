# Multimedia & Data Ecosystem: Antigravity Architecture

**WHO**: Maintained by the Antigravity Core Team and Data Science units.
**WHAT**: A highly-scalable, production-ready framework for multi-agent ecosystems processing multimedia and raw data.
**WHEN**: Deployed for continuous enterprise-grade agentic tasks requiring precise RAG grounding, data visualization, and autonomous generation workflows.
**WHERE**: Housed within the `multimedia-data-ecosystem/` root domain.
**WHY**: To eliminate "token bloat", ensuring LLMs operate under strict technical and structural constraints using the Neo-CRISPE semantic architecture.

## Architectural Topology (Graphify Map)

> [!IMPORTANT]
> As an Agent, always traverse this Graphify map first to understand the context and requirements of the ecosystem before execution.

```mermaid
graph TD
    %% Core Nodes
    A[Antigravity Ecosystem: Multimedia & Data]
    
    %% Folders
    A --> B(brain/)
    A --> C(hooks/)
    A --> D(implicit/)
    A --> E(knowledge/)
    A --> F(plugins/)
    A --> G(rules/)
    A --> H(scratch/)
    A --> I(tests/)
    A --> J(workflows/)
    
    %% Documents
    A -.-> K[DESIGN.md]
    A -.-> L[README.md]

    %% Dependencies
    B -->|Core Intelligence| J
    F -->|Agent Skills| J
    E -->|RAG / Context| B
    G -->|Constraints| B
    C -->|Triggers| J
    
    %% Plugins breakdown
    F --> F1[document-decoder-agent]
    F --> F2[image-creator-agent]
    F --> F3[video-creator-agent]
    F --> F4[audio-creator-agent]
    F --> F5[graphics-creator-agent]
    F --> F6[presentations-creator-agent]
    F --> F7[visual-decoder-agent]

    %% Styling
    classDef root fill:#0F172A,stroke:#6366F1,stroke-width:2px,color:#F8FAFC
    classDef folder fill:#1E293B,stroke:#3B82F6,stroke-width:1px,color:#E2E8F0
    classDef asset fill:#334155,stroke:#94A3B8,stroke-width:1px,color:#F1F5F9
    classDef plugin fill:#064E3B,stroke:#10B981,stroke-width:1px,color:#ECFDF5
    
    class A root
    class B,C,D,E,F,G,H,I,J folder
    class K,L asset
    class F1,F2,F3,F4,F5,F6,F7 plugin
```

## Immutable Design & Spatial Reasoning (DwT)
All subagents in this ecosystem are programmed with the **Drawing-with-Thought (DwT)** paradigm. They must compute spatial coordinates and maintain strict adherence to aesthetic variables without deviating. 
Outputs are exclusively in `kebab-case` Markdown and strictly formatted JSON arrays/objects to prevent hallucinated visual features.
