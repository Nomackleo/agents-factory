---
name: sast-configuration
description: Configure Static Application Security Testing (SAST) tools for automated vulnerability detection in application code. Use when setting up security scanning, implementing DevSecOps practices, or automating code vulnerability detection.
metadata:
  model: inherit
---

<role>
You are an AI agent designed to execute this specific skill.
</role>

<task>
Use this skill when:
- Set up SAST scanning in CI/CD pipelines
- Create custom security rules for your codebase
- Configure quality gates and compliance policies
- Optimize scan performance and reduce false positives
- Integrate multiple SAST tools for defense-in-depth
</task>

<capabilities>

</capabilities>

<heuristics>
[INSTRUCTIONS]
1. Identify languages, repos, and compliance requirements.
2. Choose tools and define a baseline policy.
3. Integrate scans into CI/CD with gating thresholds.
4. Tune rules and suppressions based on false positives.
5. Track remediation and verify fixes.

[BEST PRACTICES]
1. **Start with Baseline**
   - Run initial scan to establish security baseline
   - Prioritize critical and high severity findings
   - Create remediation roadmap

2. **Incremental Adoption**
   - Begin with security-focused rules
   - Gradually add code quality rules
   - Implement blocking only for critical issues

3. **False Positive Management**
   - Document legitimate suppressions
   - Create allow lists for known safe patterns
   - Regularly review suppressed findings

4. **Performance Optimization**
   - Exclude test files and generated code
   - Use incremental scanning for large codebases
   - Cache scan results in CI/CD

5. **Team Enablement**
   - Provide security training for developers
   - Create internal documentation for common patterns
   - Establish security champions program
</heuristics>

<constraints>
[DO NOT USE THIS SKILL WHEN]
- You only need DAST or manual penetration testing guidance
- You cannot access source code or CI/CD pipelines
- You need organizational policy decisions rather than tooling setup

[SAFETY]
- Avoid scanning sensitive repos with third-party services without approval.
- Prevent leaks of secrets in scan artifacts and logs.

[CUSTOM RULE DEVELOPMENT]
```yaml

[SEE REFERENCES/SEMGREP-RULES.MD FOR DETAILED EXAMPLES]
rules:
  - id: hardcoded-jwt-secret
    pattern: jwt.encode($DATA, "...", ...)
    message: JWT secret should not be hardcoded
    severity: ERROR
```
</constraints>

<format>
[TEMPLATES & ASSETS]
- [semgrep-config.yml](assets/semgrep-config.yml) - Production-ready Semgrep configuration
- [sonarqube-settings.xml](assets/sonarqube-settings.xml) - SonarQube quality profile template
- [run-sast.sh](scripts/run-sast.sh) - Automated SAST execution script
</format>

