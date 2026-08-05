# Google Workspace Ecosystem: Topologic Architecture & RAG Index

**WHO**: Maintained by the Enterprise Architecture & AI Knowledge Engineering teams.
**WHAT**: Architectural layout for high-performance Google Workspace / Google Drive governance, deterministic file naming, `.context.jsonld` RAG graph manifests, and `.gdriveignore` security exclusion policies.
**WHEN**: Triggered during client workspace onboarding, drive folder reorganizations, and Gemini DeepMind RAG indexing workflows.
**WHERE**: Operates entirely within the `agents-factory/google-workspace-ecosystem/` domain.
**WHY**: To guarantee Gemini DeepMind RAG readability, maintain zero data loss, eliminate file ambiguity, and enforce strict ISO 25010, ISO 42001, ISO 27001, and SOC 2 compliance.

## Vector Search Indexing Rules

> [!IMPORTANT]
> All automated agents and RAG indexers must traverse this topology to understand workspace boundaries. Data ingestion must prioritize `.agents/rules/` before executing any `.agents/workflows/`.

## Architectural Topology (Rendered by Graphify CLI)

```mermaid
graph TD
    %% Core Nodes
    A[Google Workspace Ecosystem] --> B(.agents/rules/)
    A --> C(.agents/workflows/)
    A --> D(.agents/skills/)
    A --> E(notebooklm-templates/)

    %% Rules
    B --> B1[gdrive-posix-naming-rules.md]

    %% Workflows
    C --> C1[gdrive-workspace-indexing-workflow.md]

    %% Skills
    D --> D1[gdrive-workspace-architect]

    %% Templates
    E --> E1[context.jsonld.template]
    E --> E2[gdriveignore.template]

    %% Styling
    classDef domain fill:#1E293B,stroke:#3B82F6,stroke-width:2px,color:#F8FAFC
    classDef file fill:#334155,stroke:#94A3B8,stroke-width:1px,color:#F1F5F9
    classDef agent fill:#0F172A,stroke:#10B981,stroke-width:1px,color:#E2E8F0

    class A,B,C,D,E domain
    class B1,C1,E1,E2 file
    class D1 agent
```

## ISO & NIST Standards Mapping

- **ISO 25010 (Software & Data Quality)**: Enforced via POSIX & ISO 8601 deterministic file naming (`YYYYMMDD_[SCOPE]_[ENTITY]_[TYPE]_[DESCRIPTION]_[VERSION]`).
- **ISO 42001 (AI Management System)**: Governed via `.context.jsonld` manifests specifying `aiIndexingAllowed: true/false` and node dependency trees for Gemini DeepMind.
- **ISO 27001 (Information Security)**: RBAC access control policies and `.gdriveignore` rules to exclude secrets, raw PII, and financial ledgers.
- **SOC 2 & Zero Data Loss Policy**: Prohibits file deletion or content mutation during workspace reorganization.
