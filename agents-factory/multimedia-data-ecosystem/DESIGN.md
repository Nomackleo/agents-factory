# Design Specification: Multimedia & Data Ecosystem

## System Overview
The `multimedia-data-ecosystem` is an enterprise-grade agentic factory built on top of the Antigravity SDK. It strictly adheres to the Neo-CRISPE semantic architectures to guarantee isolated, reproducible, and high-performance workflows.

## Directory Taxonomy

- **brain/**: Contains the core intelligence, memory schemas, and cognitive architectures that dictate how agents reason within this specific ecosystem.
- **hooks/**: Scripts and interceptors that trigger autonomous workflows based on external stimuli (e.g., file drops, webhook events).
- **implicit/**: Pre-computed heuristics, hidden instructions, or system prompts that are implicitly injected into agent contexts without explicit user prompts.
- **knowledge/**: Vectorized or structured documents for RAG (Retrieval-Augmented Generation). The source of truth for the ecosystem.
- **plugins/**: Specialized subagents and skills (`SKILL.md`) that extend the core capabilities (e.g., `document-decoder-agent`, `video-creator-agent`).
- **rules/**: Strict guidelines, constraints, and validation schemas that the agents must follow (e.g., JSON schemas, formatting rules).
- **scratch/**: Temporary workspace for agents to generate intermediary files, logs, or drafts before finalizing outputs.
- **tests/**: Automated verification scripts and benchmarking tests for validating agent performance and rule adherence.
- **workflows/**: High-level orchestration blueprints (e.g., YAML/JSON) that define the sequences of agent interactions.
- **DESIGN.md**: This file. Outlines the architectural and design philosophies of the ecosystem.
- **README.md**: Contains the Graphify Map for semantic routing and high-level ecosystem description.

## The 5 W's Rule
Every document, prompt, and output generated within this ecosystem MUST explicitly answer WHO, WHAT, WHEN, WHERE, and WHY in its header or first paragraphs to mitigate the "curse of knowledge".

## Performance & Quality Standards
1. **Neo-CRISPE Semantics**: XML-delimited prompt framing for maximal inference efficiency.
2. **Kebab-Case File Topologies**: All generated assets must use `kebab-case` to prevent path parsing errors.
3. **Deterministic Outputs**: Agents must rely on strict JSON objects for data passing between the extraction phase and the visualization phase. No free-text hallucination is allowed in data layers.
