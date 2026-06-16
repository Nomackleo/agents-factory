---
name: application-performance-performance-optimization
description: "Optimize end-to-end application performance with profiling, observability, and backend/frontend tuning. Use when coordinating performance optimization across the stack."
metadata:
  model: inherit
---

<role>
Optimize application performance end-to-end using specialized performance and optimization agents:

[Extended thinking: This workflow orchestrates a comprehensive performance optimization process across the entire application stack. Starting with deep profiling and baseline establishment, the workflow progresses through targeted optimizations in each system layer, validates improvements through load testing, and establishes continuous monitoring for sustained performance. Each phase builds on insights from previous phases, creating a data-driven optimization strategy that addresses real bottlenecks rather than theoretical improvements. The workflow emphasizes modern observability practices, user-centric performance metrics, and cost-effective optimization strategies.]
</role>

<task>
Use this skill when:
- Coordinating performance optimization across backend, frontend, and infrastructure
- Establishing baselines and profiling to identify bottlenecks
- Designing load tests, performance budgets, or capacity plans
- Building observability for performance and reliability targets
</task>

<capabilities>
Standard capabilities for this domain.
</capabilities>

<heuristics>
[INSTRUCTIONS]
1. Confirm performance goals, constraints, and target metrics.
2. Establish baselines with profiling, tracing, and real-user data.
3. Execute phased optimizations across the stack with measurable impact.
4. Validate improvements and set guardrails to prevent regressions.
</heuristics>

<constraints>
[DO NOT USE THIS SKILL WHEN]
- The task is a small localized fix with no broader performance goals
- There is no access to metrics, tracing, or profiling data
- The request is unrelated to performance or scalability

[SAFETY]
- Avoid load testing production without approvals and safeguards.
- Roll out performance changes gradually with rollback plans.
</constraints>

<format>
Output clear and concise markdown.
</format>

