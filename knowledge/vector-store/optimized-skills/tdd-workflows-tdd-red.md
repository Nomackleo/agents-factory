---
name: tdd-workflows-tdd-red
description: Generate failing tests for the TDD red phase to define expected behavior and edge cases.
metadata:
  model: inherit
---

<role>
Write comprehensive failing tests following TDD red phase principles.

[Extended thinking: Generates failing tests that properly define expected behavior using test-automator agent.]
</role>

<task>
Use this skill when:
- Starting the TDD red phase for new behavior
- You need failing tests that capture expected behavior
- You want edge case coverage before implementation
</task>

<capabilities>
Standard capabilities for this domain.
</capabilities>

<heuristics>
[INSTRUCTIONS]
1. Identify behaviors, constraints, and edge cases.
2. Generate failing tests that define expected outcomes.
3. Ensure failures are due to missing behavior, not setup errors.
4. Document how to run tests and verify failures.
</heuristics>

<constraints>
[DO NOT USE THIS SKILL WHEN]
- You are in the green or refactor phase
- You only need performance benchmarks
- Tests must run against production systems

[SAFETY]
- Keep test data isolated and avoid production environments.
- Avoid flaky external dependencies in the red phase.
</constraints>

<format>
[PROMPT TEMPLATE]
"Generate comprehensive FAILING tests for: $ARGUMENTS
</format>

