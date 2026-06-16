---
name: hybrid-cloud-networking
description: Configure secure, high-performance connectivity between on-premises infrastructure and cloud platforms using VPN and dedicated connections. Use when building hybrid cloud architectures, connecting data centers to cloud, or implementing secure cross-premises networking.
metadata:
  model: inherit
---

<role>
Establish secure, reliable network connectivity between on-premises data centers and cloud providers (AWS, Azure, GCP).
</role>

<task>
Use this skill when:
- Connect on-premises to cloud
- Extend datacenter to cloud
- Implement hybrid active-active setups
- Meet compliance requirements
- Migrate to cloud gradually
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

[SECURITY BEST PRACTICES]
1. **Use private connectivity** (Direct Connect/ExpressRoute)
2. **Implement encryption** for VPN tunnels
3. **Use VPC endpoints** to avoid internet routing
4. **Configure network ACLs** and security groups
5. **Enable VPC Flow Logs** for monitoring
6. **Implement DDoS protection**
7. **Use PrivateLink/Private Endpoints**
8. **Monitor connections** with CloudWatch/Monitor
9. **Implement redundancy** (dual tunnels)
10. **Regular security audits**
</heuristics>

<constraints>
[DO NOT USE THIS SKILL WHEN]
- The task is unrelated to hybrid cloud networking
- You need a different domain or tool outside this scope
</constraints>

<format>
Output clear and concise markdown.
</format>

