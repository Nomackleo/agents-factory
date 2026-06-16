---
name: github-actions-templates
description: Create production-ready GitHub Actions workflows for automated testing, building, and deploying applications. Use when setting up CI/CD with GitHub Actions, automating development workflows, or creating reusable workflow templates.
metadata:
  model: inherit
---

<role>
Create efficient, secure GitHub Actions workflows for continuous integration and deployment across various tech stacks.
</role>

<task>
Use this skill when:
- Automate testing and deployment
- Build Docker images and push to registries
- Deploy to Kubernetes clusters
- Run security scans
- Implement matrix builds for multiple environments
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

[WORKFLOW BEST PRACTICES]
1. **Use specific action versions** (@v4, not @latest)
2. **Cache dependencies** to speed up builds
3. **Use secrets** for sensitive data
4. **Implement status checks** on PRs
5. **Use matrix builds** for multi-version testing
6. **Set appropriate permissions**
7. **Use reusable workflows** for common patterns
8. **Implement approval gates** for production
9. **Add notification steps** for failures
10. **Use self-hosted runners** for sensitive workloads
</heuristics>

<constraints>
[DO NOT USE THIS SKILL WHEN]
- The task is unrelated to github actions templates
- You need a different domain or tool outside this scope
</constraints>

<format>
[GITHUB ACTIONS TEMPLATES]
Production-ready GitHub Actions workflow patterns for testing, building, and deploying applications.
</format>

