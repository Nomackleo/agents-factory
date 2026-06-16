---
name: startup-business-analyst-financial-projections
description: Create detailed 3-5 year financial model with revenue, costs, cash
  flow, and scenarios
allowed-tools: Read Write Edit Glob Grep Bash WebSearch WebFetch
metadata:
  model: inherit
---

<role>
You are an AI agent designed to execute this specific skill.
</role>

<task>
Use this skill when:
- Working on financial projections tasks or workflows
- Needing guidance, best practices, or checklists for financial projections
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

[FINANCIAL MODEL BEST PRACTICES]
**Do:**
- Use cohort-based revenue model
- Include 3 scenarios
- Show monthly detail (Year 1-2)
- Calculate key metrics
- Validate against benchmarks
- Document all assumptions
- Show cash flow and runway
- Include fundraising milestones

**Don't:**
- Be overly optimistic on growth
- Underestimate costs
- Forget fully-loaded compensation
- Ignore cash timing
- Skip scenario analysis
- Use static headcount
- Forget to validate
</heuristics>

<constraints>
[DO NOT USE THIS SKILL WHEN]
- The task is unrelated to financial projections
- You need a different domain or tool outside this scope
</constraints>

<format>
Output clear and concise markdown.
</format>

