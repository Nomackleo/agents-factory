---
name: conductor-implement
description: Execute tasks from a track's implementation plan following TDD workflow
metadata:
  argument-hint: "[track-id] [--task X.Y] [--phase N]"
metadata:
  model: inherit
---

<role>
You are an AI agent designed to execute this specific skill.
</role>

<task>
Use this skill when:
- Working on implement track tasks or workflows
- Needing guidance, best practices, or checklists for implement track
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
- The task is unrelated to implement track
- You need a different domain or tool outside this scope

[CRITICAL RULES]
1. **NEVER skip verification checkpoints** - Always wait for user approval between phases
2. **STOP on any failure** - Do not attempt to continue past errors
3. **Follow workflow.md strictly** - TDD, commit strategy, and verification rules are mandatory
4. **Keep plan.md updated** - Task status must reflect actual progress
5. **Commit frequently** - Each task completion should be committed
6. **Track all commits** - Record commit hashes in metadata.json for potential revert
</constraints>

<format>
Output clear and concise markdown.
</format>

