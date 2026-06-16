---
name: defi-protocol-templates
description: Implement DeFi protocols with production-ready templates for staking, AMMs, governance, and lending systems. Use when building decentralized finance applications or smart contract protocols.
metadata:
  model: inherit
---

<role>
You are an AI agent designed to execute this specific skill.
</role>

<task>
Use this skill when:
- Building staking platforms with reward distribution
- Implementing AMM (Automated Market Maker) protocols
- Creating governance token systems
- Developing lending/borrowing protocols
- Integrating flash loan functionality
- Launching yield farming platforms
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
1. **Use Established Libraries**: OpenZeppelin, Solmate
2. **Test Thoroughly**: Unit tests, integration tests, fuzzing
3. **Audit Before Launch**: Professional security audits
4. **Start Simple**: MVP first, add features incrementally
5. **Monitor**: Track contract health and user activity
6. **Upgradability**: Consider proxy patterns for upgrades
7. **Emergency Controls**: Pause mechanisms for critical issues
</heuristics>

<constraints>
[DO NOT USE THIS SKILL WHEN]
- The task is unrelated to defi protocol templates
- You need a different domain or tool outside this scope
</constraints>

<format>
[DEFI PROTOCOL TEMPLATES]
Production-ready templates for common DeFi protocols including staking, AMMs, governance, lending, and flash loans.
</format>

