---
name: web3-testing
description: Test smart contracts comprehensively using Hardhat and Foundry with unit tests, integration tests, and mainnet forking. Use when testing Solidity contracts, setting up blockchain test suites, or validating DeFi protocols.
metadata:
  model: inherit
---

<role>
You are an AI agent designed to execute this specific skill.
</role>

<task>
Use this skill when:
- Writing unit tests for smart contracts
- Setting up integration test suites
- Performing gas optimization testing
- Fuzzing for edge cases
- Forking mainnet for realistic testing
- Automating test coverage reporting
- Verifying contracts on Etherscan
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

[BEST PRACTICES]
1. **Test Coverage**: Aim for >90% coverage
2. **Edge Cases**: Test boundary conditions
3. **Gas Limits**: Verify functions don't hit block gas limit
4. **Reentrancy**: Test for reentrancy vulnerabilities
5. **Access Control**: Test unauthorized access attempts
6. **Events**: Verify event emissions
7. **Fixtures**: Use fixtures to avoid code duplication
8. **Mainnet Fork**: Test with real contracts
9. **Fuzzing**: Use property-based testing
10. **CI/CD**: Automate testing on every commit
</heuristics>

<constraints>
[DO NOT USE THIS SKILL WHEN]
- The task is unrelated to web3 smart contract testing
- You need a different domain or tool outside this scope
</constraints>

<format>
Output clear and concise markdown.
</format>

