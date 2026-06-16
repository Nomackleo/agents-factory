---
name: workflow-patterns
description: Use this skill when implementing tasks according to Conductor's TDD
  workflow, handling phase checkpoints, managing git commits for tasks, or
  understanding the verification protocol.
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
- Implementing tasks from a track's plan.md
- Following TDD red-green-refactor cycle
- Completing phase checkpoints
- Managing git commits and notes
- Understanding quality assurance gates
- Handling verification protocols
- Recording progress in plan files
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
- The task is unrelated to workflow patterns
- You need a different domain or tool outside this scope
</constraints>

<format>
Output clear and concise markdown.
</format>

