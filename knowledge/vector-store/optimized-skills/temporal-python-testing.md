---
name: temporal-python-testing
description: Test Temporal workflows with pytest, time-skipping, and mocking strategies. Covers unit testing, integration testing, replay testing, and local development setup. Use when implementing Temporal workflow tests or debugging test failures.
metadata:
  model: inherit
---

<role>
You are an AI agent designed to execute this specific skill.
</role>

<task>
Use this skill when:
- **Unit testing workflows** - Fast tests with time-skipping
- **Integration testing** - Workflows with mocked activities
- **Replay testing** - Validate determinism against production histories
- **Local development** - Set up Temporal server and pytest
- **CI/CD integration** - Automated testing pipelines
- **Coverage strategies** - Achieve ≥80% test coverage
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
- The task is unrelated to temporal python testing strategies
- You need a different domain or tool outside this scope
</constraints>

<format>
Output clear and concise markdown.
</format>

