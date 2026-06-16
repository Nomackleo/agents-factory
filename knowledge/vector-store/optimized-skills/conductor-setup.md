---
name: conductor-setup
description: Initialize project with Conductor artifacts (product definition,
  tech stack, workflow, style guides)
metadata:
  argument-hint: "[--resume]"
metadata:
  model: inherit
---

<role>
You are an AI agent designed to execute this specific skill.
</role>

<task>
Use this skill when:
- Working on conductor setup tasks or workflows
- Needing guidance, best practices, or checklists for conductor setup
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
</heuristics>

<constraints>
[DO NOT USE THIS SKILL WHEN]
- The task is unrelated to conductor setup
- You need a different domain or tool outside this scope
</constraints>

<format>
Output clear and concise markdown.
</format>

