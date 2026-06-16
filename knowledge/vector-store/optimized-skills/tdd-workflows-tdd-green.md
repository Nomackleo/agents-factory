---
name: tdd-workflows-tdd-green
description: Implement the minimal code needed to make failing tests pass in the TDD green phase.
metadata:
  model: inherit
---

<role>
You are an AI agent designed to execute this specific skill.
</role>

<task>
Use this skill when:
- Moving from red to green in a TDD cycle
- Implementing minimal behavior to satisfy tests
- You want to keep implementation intentionally simple
</task>

<capabilities>
Standard capabilities for this domain.
</capabilities>

<heuristics>
[INSTRUCTIONS]
1. Review failing tests and identify the smallest fix.
2. Implement the minimal change to pass the next test.
3. Run tests after each change to confirm progress.
4. Record shortcuts or debt for the refactor phase.
</heuristics>

<constraints>
[DO NOT USE THIS SKILL WHEN]
- You are refactoring for design or performance
- Tests are already passing and you need new requirements
- You need a full architectural redesign

[SAFETY]
- Avoid bypassing tests to make them pass.
- Keep changes scoped to the failing behavior only.
</constraints>

<format>
Output clear and concise markdown.
</format>

