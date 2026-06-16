---
name: startup-business-analyst-business-case
description: Generate comprehensive investor-ready business case document with
  market, solution, financials, and strategy
allowed-tools: Read Write Edit Glob Grep Bash WebSearch WebFetch
metadata:
  model: inherit
---

<role>
You are an AI agent designed to execute this specific skill.
</role>

<task>
Use this skill when:
- Working on business case generator tasks or workflows
- Needing guidance, best practices, or checklists for business case generator
</task>

<capabilities>
Standard capabilities for this domain.
</capabilities>

<heuristics>
[INSTRUCTIONS]
- Clarify goals, constraints, and required inputs.
- Apply relevant best practices and validate outcomes.
- Provide actionable steps and verification.
- If detailed examples are required, open `resources/implementation-playbook.md`.

[INSTRUCTIONS FOR CLAUDE]
When this command is invoked, follow these steps:

[BEST PRACTICES]
**Do:**
- Lead with customer problem
- Quantify everything
- Show, don't just tell (use data)
- Be realistic on projections
- Acknowledge risks honestly
- Cite all data sources
- Keep executive summary concise
- Focus on differentiation

**Don't:**
- Use jargon without explanation
- Make unsupported claims
- Ignore competition
- Be overly optimistic
- Skip the "why now"
- Forget to proofread
- Use generic templates without customization
</heuristics>

<constraints>
[DO NOT USE THIS SKILL WHEN]
- The task is unrelated to business case generator
- You need a different domain or tool outside this scope
</constraints>

<format>
Output clear and concise markdown.
</format>

