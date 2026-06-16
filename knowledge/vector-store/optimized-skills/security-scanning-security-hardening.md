---
name: security-scanning-security-hardening
description: "Coordinate multi-layer security scanning and hardening across application, infrastructure, and compliance controls."
metadata:
  model: inherit
---

<role>
Implement comprehensive security hardening with defense-in-depth strategy through coordinated multi-agent orchestration:

[Extended thinking: This workflow implements a defense-in-depth security strategy across all application layers. It coordinates specialized security agents to perform comprehensive assessments, implement layered security controls, and establish continuous security monitoring. The approach follows modern DevSecOps principles with shift-left security, automated scanning, and compliance validation. Each phase builds upon previous findings to create a resilient security posture that addresses both current vulnerabilities and future threats.]
</role>

<task>
Use this skill when:
- Running a coordinated security hardening program
- Establishing defense-in-depth controls across app, infra, and CI/CD
- Prioritizing remediation from scans and threat modeling
</task>

<capabilities>
Standard capabilities for this domain.
</capabilities>

<heuristics>
[INSTRUCTIONS]
1. Execute Phase 1 to establish a security baseline.
2. Apply Phase 2 remediations for high-risk issues.
3. Implement Phase 3 controls and validate defenses.
4. Complete Phase 4 validation and compliance checks.
</heuristics>

<constraints>
[DO NOT USE THIS SKILL WHEN]
- You only need a quick scan without remediation work
- You lack authorization for security testing or changes
- The environment cannot tolerate invasive security controls

[SAFETY]
- Avoid intrusive testing in production without approval.
- Ensure rollback plans exist before hardening changes.
</constraints>

<format>
Output clear and concise markdown.
</format>

