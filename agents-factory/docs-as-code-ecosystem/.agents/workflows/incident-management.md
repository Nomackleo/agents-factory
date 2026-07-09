# Workflow: Critical Incident Resolution Pipeline

**WHO**: SRE Architect Agent, Engineering Technical Writer Agent, Legal Advisor Agent.
**WHAT**: A multi-agent pipeline for resolving critical production incidents, documenting the RCA, and reviewing compliance.
**WHEN**: Triggered during SEV1 or SEV2 active incidents or immediately post-resolution.
**WHERE**: Executed within the `docs-as-code-ecosystem`.
**WHY**: To ensure rapid stabilization followed by a blameless, ISO-compliant post-mortem that reduces future error budget consumption.

## Workflow Execution Steps

### 1. Incident Command (SRE Architect)
- **Action**: The user provides the incident context/logs.
- **Agent**: `sre-architect`
- **Output**: The SRE Architect generates immediate mitigation steps and stabilization commands.

### 2. RCA and Post-Mortem Draft (SRE Architect -> Technical Writer)
- **Action**: Once the system is stable, `sre-architect` performs the blameless RCA.
- **Handoff**: The raw RCA notes are passed to `engineering-technical-writer`.
- **Output**: The Technical Writer formats a pristine `kebab-case` Markdown Post-Mortem incorporating the 5 W's, timelines, and action items.

### 3. Compliance and Liability Review (Legal Advisor)
- **Action**: If the incident involved data breaches (PII/PHI) or SLA violations.
- **Agent**: `legal-advisor`
- **Output**: Reviews the Post-Mortem, generates necessary compliance notifications (e.g., GDPR 72-hour notification draft), and ensures liability disclaimers are correctly applied.

### 4. Runbook Update (SRE Architect)
- **Action**: Based on the new RCA findings.
- **Agent**: `sre-architect`
- **Output**: A new or updated `incident-runbook` stored in the enterprise system monorepo.
