# Multimedia & Data Ecosystem: Topologic Architecture & RAG Index

**WHO**: Maintained by the Data Science and Creative Arts units. Designed for advanced socio-political researchers and multimedia directors.
**WHAT**: This ecosystem governs the end-to-end pipeline from rigorous data triangulation (via NotebookLM) to generative art, graphic design, and audiovisual creation (via specialized Gemini agents).
**WHEN**: Triggered when raw sociopolitical, economic, and historical datasets must be abstracted and transformed into high-fidelity visual or audiovisual formats.
**WHERE**: Operates across the `multimedia-data-ecosystem/` bridging NotebookLM source-grounding with Antigravity/Gemini generative engines.
**WHY**: To eliminate AI hallucinations in political/historical context by grounding generation strictly in verified data, while maintaining absolute aesthetic control through strict JSON-driven prompt engineering (Nano Banana 2 / Omni).

## Vector Search Indexing Rules
> [!IMPORTANT]
> This ecosystem enforces the Separation of Visualization Content principle. RAG engines must identify data extraction rules from `notebooklm-templates/` and delegate formatting/aesthetic reasoning to the `agents/` specialized JSON outputs.

## Architectural Topology (Graphify Map)

```mermaid
graph TD
    %% Core Nodes
    A[Multimedia & Data Ecosystem] --> B(notebooklm-templates/)
    A --> C(agents/)

    %% NotebookLM
    B --> B1[notebook-instructions.md]
    B --> B2[chat-instructions.md]
    B --> B3[studio-instructions.md]
    
    %% Gemini Agents
    C --> C1[visual-decoder-agent]
    C --> C2[image-creator-agent]
    C --> C3[video-creator-agent]
    C --> C4[audio-creator-agent]

    %% Interactions (Data Flow)
    B1 -->|Raw Data| B2
    B2 -->|Statistical JSON| C2
    B3 -->|Creative Brief| C1
    C1 -->|Aesthetic JSON| C2
    C1 -->|Aesthetic JSON| C3
    
    %% Styling
    classDef domain fill:#1E293B,stroke:#8B5CF6,stroke-width:2px,color:#F8FAFC
    classDef file fill:#334155,stroke:#C4B5FD,stroke-width:1px,color:#F1F5F9
    classDef agent fill:#0F172A,stroke:#F59E0B,stroke-width:1px,color:#E2E8F0
    
    class A domain
    class B,C file
    class B1,B2,B3 file
    class C1,C2,C3,C4 agent
```

## Immutable Design & Spatial Reasoning (DwT)
All agents in this ecosystem are programmed with the **Drawing-with-Thought (DwT)** paradigm. They must compute spatial coordinates and maintain strict adherence to aesthetic variables without deviating. 
Outputs are exclusively in `kebab-case` Markdown and strictly formatted JSON arrays/objects to prevent hallucinated visual features.
