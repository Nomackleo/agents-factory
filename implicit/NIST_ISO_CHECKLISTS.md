# NIST CSF 2.0, ISO 42001 & ISO 27001: Cybersecurity and AI Management Checklists

**Reference Notebook**: `NIST CSF 2.0 and ISO 42001, 27001: Cybersecurity and AI Management` (Gemini Notebook RAG)  
**Scope**: Universal Business & Technical Compliance Rules for Antigravity Agent Factory

---

## 1. NIST Cybersecurity Framework (CSF) 2.0 Checklists

### 1.1 GOVERN (GV) - AI & Security Governance

- [ ] **GV.OC-01**: Define organizational security context, enterprise risk tolerance, and AI ethics policy.
- [ ] **GV.RM-01**: Establish risk management strategy covering autonomous agents, LLM tool execution, and prompt injection threat vectors.
- [ ] **GV.PO-01**: Enforce mandatory human-in-the-loop (HITL) approval gates before executing destructive tools or writing outside sandbox boundaries.
- [ ] **GV.SC-01**: Supply Chain Risk Management — Audit third-party MCP servers, API plugins, and model endpoints.

### 1.2 IDENTIFY (ID) - Asset & AI Model Inventory

- [ ] **ID.AM-01**: Maintain a dynamic asset inventory of all deployed agents (`agents-factory/`), skills (`.agents/skills/`), and SQLite vector DB instances (`Codebase-Memory-MCP`).
- [ ] **ID.RA-01**: Conduct AI impact assessments (AIIA) and data privacy impact assessments (DPIA) prior to agent deployment.
- [ ] **ID.IM-01**: Track model lineage, context window bounds, temperature settings, and `thinking_level` configurations per agent role.

### 1.3 PROTECT (PR) - Zero Trust & Data Protection

- [ ] **PR.AA-01**: Identity and Access Management — Enforce strict role isolation in subagents (`00-supervisor-router`, `01-research-gatherer`, `02-workflow-architect`, `03-crispe-generator`).
- [ ] **PR.DS-01**: Data Security — Filter secrets (API keys, JWTs, OAuth tokens) in the `PreToolUse` hook before LLM context injection.
- [ ] **PR.PS-01**: Platform Security — Restrict code execution to `scratch/` and `agents-factory/` sandboxes.
- [ ] **PR.IR-01**: Infrastructure Resilience — Enforce non-destructive execution rules and input sanitization on web search outputs.

### 1.4 DETECT (DE) - Continuous Monitoring & Anomaly Detection

- [ ] **DE.CM-01**: Log all tool calls, argument payloads, and LLM responses with deterministic trace IDs.
- [ ] **DE.AE-01**: Detect indirect prompt injections, Unicode obfuscation, and Base64-encoded instruction overrides in real time.
- [ ] **DE.CM-02**: Audit token usage spikes and anomalous recursive subagent spawning.

### 1.5 RESPOND (RS) - Incident Management

- [ ] **RS.MA-01**: Dead-man Switch — Automatically terminate subagent loops exceeding `max_turns` or failing token economic thresholds.
- [ ] **RS.MI-01**: Roll back filesystem state and purge compromised context buffers upon detecting security violations.

### 1.6 RECOVER (RC) - Restoration & Continuous Learning

- [ ] **RC.RP-01**: Re-ingest clean architectural blueprints from `Codebase-Memory-MCP` (SQLite) post-incident.
- [ ] **RC.CO-01**: Post-incident review: Extract lessons learned into `.agents/skills/staging/` via the `Stop` hook (`/learn`).

---

## 2. ISO 42001: Artificial Intelligence Management System (AIMS) Checklists

### 2.1 AI Risk Assessment & System Impact (Clause 6.1)

- [ ] **AIMS-RA-01**: Evaluate safety, privacy, bias, and operational risks across the full agent lifecycle.
- [ ] **AIMS-RA-02**: Enforce model routing rules based on task complexity (e.g., `gemini-3.8-flash` with appropriate `thinking_level`).

### 2.2 Data Governance for AI Systems (Clause 7.5)

- [ ] **AIMS-DG-01**: Verify provenance and exegesis of research data ingested by `01-research-gatherer`.
- [ ] **AIMS-DG-02**: Prevent data leakage into prompt context using sanitization filters in `PreToolUse`.

### 2.3 Algorithmic Transparency & Auditability (Clause 8.2)

- [ ] **AIMS-AT-01**: Require structured XML payloads (`<corporate_context>`, `<reasoning_trace>`) for inter-agent handoffs.
- [ ] **AIMS-AT-02**: Document all prompt templates using the Neo-CRISPE framework (Capacity, Role, Instruction, Schema, Personality, Examples).

### 2.4 Human Oversight & Control (Clause 8.4)

- [ ] **AIMS-HO-01**: Implement mandatory HITL review before committing generated skills or production code to disk.
- [ ] **AIMS-HO-02**: Allow human override and immediate process kill via the `manage_task` tool.

---

## 3. ISO 27001: Information Security Management (ISMS) Checklists

### 3.1 Security Policies & Access Control (A.5 / A.9)

- [ ] **ISMS-AC-01**: Least-Privilege access for MCP tools (read-only filesystem access where applicable, sandboxed execution).
- [ ] **ISMS-AC-02**: Enforce credential separation — zero hardcoded API keys in `models.yml` or agent prompts.

### 3.2 Cryptography & Data Protection (A.10 / A.8)

- [ ] **ISMS-DP-01**: Encrypt workspace memory databases (SQLite) and local vector stores.
- [ ] **ISMS-DP-02**: Strip PII (Personally Identifiable Information) and confidential enterprise data before sending payloads to external web APIs.

### 3.3 Operations Security & Vulnerability Management (A.12 / A.14)

- [ ] **ISMS-OP-01**: Validate dependencies and scripts in `bin/` (`handoff-validator.py`, `graphify`).
- [ ] **ISMS-OP-02**: Maintain isolated staging environments for unverified skills (`.agents/skills/staging/`).

---

## 4. DORA (Digital Operational Resilience Act) Metrics & Controls

### 4.1 ICT Risk Management & Testing

- [ ] **DORA-RM-01**: Perform automated static code analysis and A/B testing in `tests/factory-ab-testing/`.
- [ ] **DORA-RM-02**: Monitor lead time for changes and change failure rate on generated agent stacks.

### 4.2 Incident Classification & Service Restoration

- [ ] **DORA-MTTR-01**: Target Time to Restore Service (MTTR) < 60 seconds using deterministic fallback to low-latency models (`gemini-3.8-flash` / `gemini-3.7-flash`).
- [ ] **DORA-RPO-01**: Zero context loss: persist session checkpoints into `brain/sessions/` on every `Stop` event.

---

## 5. RAG Integration Mapping (Gemini Notebook)

```text
 [ Gemini Notebook: NIST CSF 2.0 & ISO 42001/27001 ]
                        |
                        v  (Ingestion via nlm CLI)
 +-----------------------------------------------------+
 |  knowledge/ vector store & SQLite Codebase-Memory   |
 +-----------------------------------------------------+
                        |
                        v  (Injected into System Prompts)
 +-----------------------------------------------------+
 |  implicit/NIST_ISO_CHECKLISTS.md & GEMINI.md        |
 +-----------------------------------------------------+
```
