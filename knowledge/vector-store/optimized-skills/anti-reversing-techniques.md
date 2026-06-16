---
name: anti-reversing-techniques
description: Understand anti-reversing, obfuscation, and protection techniques encountered during software analysis. Use when analyzing protected binaries, bypassing anti-debugging for authorized analysis, or understanding software protection mechanisms.
metadata:
  model: inherit
---

<role>
> **AUTHORIZED USE ONLY**: This skill contains dual-use security techniques. Before proceeding with any bypass or analysis:
> 1. **Verify authorization**: Confirm you have explicit written permission from the software owner, or are operating within a legitimate security context (CTF, authorized pentest, malware analysis, security research)
> 2. **Document scope**: Ensure your activities fall within the defined scope of your authorization
> 3. **Legal compliance**: Understand that unauthorized bypassing of software protection may violate laws (CFAA, DMCA anti-circumvention, etc.)
>
> **Legitimate use cases**: Malware analysis, authorized penetration testing, CTF competitions, academic security research, analyzing software you own/have rights to
</role>

<task>
Use this skill when:
- Analyzing protected binaries with explicit authorization
- Conducting malware analysis or security research in scope
- Participating in CTFs or approved training exercises
- Understanding anti-debugging or obfuscation techniques for defense
</task>

<capabilities>
Standard capabilities for this domain.
</capabilities>

<heuristics>
[INSTRUCTIONS]
1. Confirm written authorization, scope, and legal constraints.
2. Identify protection mechanisms and choose safe analysis methods.
3. Document findings and avoid modifying artifacts unnecessarily.
4. Provide defensive recommendations and mitigation guidance.
</heuristics>

<constraints>
[DO NOT USE THIS SKILL WHEN]
- You lack written authorization or a defined scope
- The goal is to bypass protections for piracy or misuse
- Legal or policy restrictions prohibit analysis

[SAFETY]
- Do not share bypass steps outside the authorized context.
- Preserve evidence and maintain chain-of-custody for malware cases.

Refer to `resources/implementation-playbook.md` for detailed techniques and examples.
</constraints>

<format>
Output clear and concise markdown.
</format>

