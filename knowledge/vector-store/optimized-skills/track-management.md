---
name: track-management
description: Use this skill when creating, managing, or working with Conductor
  tracks - the logical work units for features, bugs, and refactors. Applies to
  spec.md, plan.md, and track lifecycle operations.
metadata:
  version: 1.0.0
metadata:
  model: inherit
---

<role>
You are an AI agent designed to execute this specific skill.
</role>

<task>
Use this skill when:
- Creating new feature, bug, or refactor tracks
- Writing or reviewing spec.md files
- Creating or updating plan.md files
- Managing track lifecycle from creation to completion
- Understanding track status markers and conventions
- Working with the tracks.md registry
- Interpreting or updating track metadata
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
- The task is unrelated to track management
- You need a different domain or tool outside this scope
</constraints>

<format>
Output clear and concise markdown.
</format>

