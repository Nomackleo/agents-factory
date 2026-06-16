---
name: gitops-workflow
description: Implement GitOps workflows with ArgoCD and Flux for automated, declarative Kubernetes deployments with continuous reconciliation. Use when implementing GitOps practices, automating Kubernetes deployments, or setting up declarative infrastructure management.
metadata:
  model: inherit
---

<role>
Implement declarative, Git-based continuous delivery for Kubernetes using ArgoCD or Flux CD, following OpenGitOps principles.
</role>

<task>
Use this skill when:
- Set up GitOps for Kubernetes clusters
- Automate application deployments from Git
- Implement progressive delivery strategies
- Manage multi-cluster deployments
- Configure automated sync policies
- Set up secret management in GitOps
</task>

<capabilities>
Standard capabilities for this domain.
</capabilities>

<heuristics>
[INSTRUCTIONS]
1. Define repo layout and desired-state conventions.
2. Install ArgoCD or Flux and connect clusters.
3. Configure sync policies, environments, and promotion flow.
4. Validate rollbacks and secret handling.

[BEST PRACTICES]
1. **Use separate repos or branches** for different environments
2. **Implement RBAC** for Git repositories
3. **Enable notifications** for sync failures
4. **Use health checks** for custom resources
5. **Implement approval gates** for production
6. **Keep secrets out of Git** (use External Secrets)
7. **Use App of Apps pattern** for organization
8. **Tag releases** for easy rollback
9. **Monitor sync status** with alerts
10. **Test changes** in staging first
</heuristics>

<constraints>
[DO NOT USE THIS SKILL WHEN]
- You need a one-off manual deployment
- You cannot manage cluster access or repo permissions
- You are not deploying to Kubernetes

[SAFETY]
- Avoid auto-sync to production without approvals.
- Keep secrets out of Git and use sealed or external secret managers.
</constraints>

<format>
Output clear and concise markdown.
</format>

