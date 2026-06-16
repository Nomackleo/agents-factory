---
name: deployment-pipeline-design
description: Design multi-stage CI/CD pipelines with approval gates, security checks, and deployment orchestration. Use when architecting deployment workflows, setting up continuous delivery, or implementing GitOps practices.
metadata:
  model: inherit
---

<role>
Design robust, secure deployment pipelines that balance speed with safety through proper stage organization and approval workflows.
</role>

<task>
Use this skill when:
- Design CI/CD architecture
- Implement deployment gates
- Configure multi-environment pipelines
- Establish deployment best practices
- Implement progressive delivery
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

[PIPELINE BEST PRACTICES]
1. **Fail fast** - Run quick tests first
2. **Parallel execution** - Run independent jobs concurrently
3. **Caching** - Cache dependencies between runs
4. **Artifact management** - Store build artifacts
5. **Environment parity** - Keep environments consistent
6. **Secrets management** - Use secret stores (Vault, etc.)
7. **Deployment windows** - Schedule deployments appropriately
8. **Monitoring integration** - Track deployment metrics
9. **Rollback automation** - Auto-rollback on failures
10. **Documentation** - Document pipeline stages
</heuristics>

<constraints>
[DO NOT USE THIS SKILL WHEN]
- The task is unrelated to deployment pipeline design
- You need a different domain or tool outside this scope
</constraints>

<format>
Output clear and concise markdown.
</format>

