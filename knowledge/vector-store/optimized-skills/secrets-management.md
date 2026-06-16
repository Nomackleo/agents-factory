---
name: secrets-management
description: Implement secure secrets management for CI/CD pipelines using Vault, AWS Secrets Manager, or native platform solutions. Use when handling sensitive credentials, rotating secrets, or securing CI/CD environments.
metadata:
  model: inherit
---

<role>
Implement secure secrets management in CI/CD pipelines without hardcoding sensitive information.
</role>

<task>
Use this skill when:
- Store API keys and credentials
- Manage database passwords
- Handle TLS certificates
- Rotate secrets automatically
- Implement least-privilege access
</task>

<capabilities>
Standard capabilities for this domain.
</capabilities>

<heuristics>
[INSTRUCTIONS]
1. Identify secret types, owners, and rotation requirements.
2. Choose a secrets backend and access model.
3. Integrate CI/CD or runtime retrieval with least privilege.
4. Validate rotation and audit logging.

[BEST PRACTICES]
1. **Never commit secrets** to Git
2. **Use different secrets** per environment
3. **Rotate secrets regularly**
4. **Implement least-privilege access**
5. **Enable audit logging**
6. **Use secret scanning** (GitGuardian, TruffleHog)
7. **Mask secrets in logs**
8. **Encrypt secrets at rest**
9. **Use short-lived tokens** when possible
10. **Document secret requirements**
</heuristics>

<constraints>
[DO NOT USE THIS SKILL WHEN]
- You plan to hardcode secrets in source control
- You cannot secure access to the secrets backend
- You only need local development values without sharing

[SAFETY]
- Never commit secrets to source control.
- Limit access and log secret usage for auditing.
</constraints>

<format>
Output clear and concise markdown.
</format>

