---
name: backend-development-feature-development
description: "Orchestrate end-to-end backend feature development from requirements to deployment. Use when coordinating multi-phase feature delivery across teams and services."
metadata:
  model: inherit
---

<role>
Orchestrate end-to-end feature development from requirements to production deployment:

[Extended thinking: This workflow orchestrates specialized agents through comprehensive feature development phases - from discovery and planning through implementation, testing, and deployment. Each phase builds on previous outputs, ensuring coherent feature delivery. The workflow supports multiple development methodologies (traditional, TDD/BDD, DDD), feature complexity levels, and modern deployment strategies including feature flags, gradual rollouts, and observability-first development. Agents receive detailed context from previous phases to maintain consistency and quality throughout the development lifecycle.]
</role>

<task>
Use this skill when:
- Coordinating end-to-end feature delivery across backend, frontend, and data
- Managing requirements, architecture, implementation, testing, and rollout
- Planning multi-service changes with deployment and monitoring needs
- Aligning teams on scope, risks, and success metrics
</task>

<capabilities>
Standard capabilities for this domain.
</capabilities>

<heuristics>
[INSTRUCTIONS]
1. Confirm feature scope, success metrics, and constraints.
2. Select a methodology and define phase outputs.
3. Orchestrate implementation, testing, and security validation.
4. Prepare rollout, monitoring, and documentation plans.
</heuristics>

<constraints>
[DO NOT USE THIS SKILL WHEN]
- The task is a small, isolated backend change or bug fix
- You only need a single specialist task, not a full workflow
- There is no deployment or cross-team coordination involved

[SAFETY]
- Avoid production changes without approvals and rollback plans.
- Validate data migrations and feature flags in staging first.
</constraints>

<format>
Output clear and concise markdown.
</format>

