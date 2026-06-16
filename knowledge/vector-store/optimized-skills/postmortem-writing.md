---
name: postmortem-writing
description: Write effective blameless postmortems with root cause analysis, timelines, and action items. Use when conducting incident reviews, writing postmortem documents, or improving incident response processes.
metadata:
  model: inherit
---

<role>
You are an AI agent designed to execute this specific skill.
</role>

<task>
Use this skill when:
- Conducting post-incident reviews
- Writing postmortem documents
- Facilitating blameless postmortem meetings
- Identifying root causes and contributing factors
- Creating actionable follow-up items
- Building organizational learning culture
</task>

<capabilities>

</capabilities>

<heuristics>
[INSTRUCTIONS]
- Clarify goals, constraints, and required inputs.
- Apply relevant best practices and validate outcomes.
- Provide actionable steps and verification.
- If detailed examples are required, open `resources/implementation-playbook.md`.

[BEST PRACTICES]
</heuristics>

<constraints>
[DO NOT USE THIS SKILL WHEN]
- The task is unrelated to postmortem writing
- You need a different domain or tool outside this scope

[WHY #5: WHY ISN'T THERE A SAFETY NET FOR THIS TYPE OF CHANGE?]
**Answer**: We lack automated tests that verify connection pool behavior and lack documentation about our connection patterns.

**Evidence**: Test suite has no tests for connection handling; wiki has no article on database connections.
</constraints>

<format>
[TEMPLATES]


[TEMPLATE 1: STANDARD POSTMORTEM]
```markdown

[TEMPLATE 2: 5 WHYS ANALYSIS]
```markdown

[TEMPLATE 3: QUICK POSTMORTEM (MINOR INCIDENTS)]
```markdown
</format>

