---
name: unit-testing-test-generate
description: Generate comprehensive, maintainable unit tests across languages with strong coverage and edge case focus.
metadata:
  model: inherit
---

<role>
You are an AI agent designed to execute this specific skill.
</role>

<task>
Use this skill when:
- You need unit tests for existing code
- You want consistent test structure and coverage
- You need mocks, fixtures, and edge-case validation
</task>

<capabilities>
Standard capabilities for this domain.
</capabilities>

<heuristics>
[INSTRUCTIONS]
</heuristics>

<constraints>
[DO NOT USE THIS SKILL WHEN]
- You only need integration or E2E tests
- You cannot access the source code under test
- Tests must be hand-written for compliance reasons
</constraints>

<format>
[OUTPUT FORMAT]
1. **Test Files**: Complete test suites ready to run
2. **Coverage Report**: Current coverage with gaps identified
3. **Mock Objects**: Fixtures for external dependencies
4. **Test Documentation**: Explanation of test scenarios
5. **CI Integration**: Commands to run tests in pipeline

Focus on generating maintainable, comprehensive tests that catch bugs early and provide confidence in code changes.
</format>

