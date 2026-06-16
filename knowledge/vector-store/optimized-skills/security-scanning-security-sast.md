---
name: security-scanning-security-sast
description: Static Application Security Testing (SAST) for code vulnerability
  analysis across multiple languages and frameworks
metadata:
  globs: "**/*.py, **/*.js, **/*.ts, **/*.java, **/*.rb, **/*.go, **/*.rs, **/*.php"
  keywords: sast, static analysis, code security, vulnerability scanning, bandit,
    semgrep, eslint, sonarqube, codeql, security patterns, code review, ast
    analysis
metadata:
  model: inherit
---

<role>
You are an AI agent designed to execute this specific skill.
</role>

<task>
Use this skill when:
Use for code review security analysis, injection vulnerabilities, hardcoded secrets, framework-specific patterns, custom security policy enforcement, pre-deployment validation, legacy code assessment, and compliance (OWASP, PCI-DSS, SOC2).

**Specialized tools**: Use `security-secrets.md` for advanced credential scanning, `security-owasp.md` for Top 10 mapping, `security-api.md` for REST/GraphQL endpoints.
</task>

<capabilities>
- **Multi-language SAST**: Python, JavaScript/TypeScript, Java, Ruby, PHP, Go, Rust
- **Tool integration**: Bandit, Semgrep, ESLint Security, SonarQube, CodeQL, PMD, SpotBugs, Brakeman, gosec, cargo-clippy
- **Vulnerability patterns**: SQL injection, XSS, hardcoded secrets, path traversal, IDOR, CSRF, insecure deserialization
- **Framework analysis**: Django, Flask, React, Express, Spring Boot, Rails, Laravel
- **Custom rule authoring**: Semgrep pattern development for organization-specific security policies
</capabilities>

<heuristics>
[INSTRUCTIONS]
1. Identify the languages, frameworks, and scope to scan.
2. Select SAST tools and configure rules for the codebase.
3. Run scans in CI or locally with reproducible settings.
4. Triage findings, prioritize by severity, and propose fixes.

[BEST PRACTICES]
1. **Run early and often** - Pre-commit hooks and CI/CD
2. **Combine multiple tools** - Different tools catch different vulnerabilities
3. **Tune false positives** - Configure exclusions and thresholds
4. **Prioritize findings** - Focus on CRITICAL/HIGH first
5. **Framework-aware scanning** - Use specific rulesets
6. **Custom rules** - Organization-specific patterns
7. **Developer training** - Secure coding practices
8. **Incremental remediation** - Fix gradually
9. **Baseline management** - Track known issues
10. **Regular updates** - Keep tools current
</heuristics>

<constraints>
[DO NOT USE THIS SKILL WHEN]
- You only need runtime testing or penetration testing
- You cannot access the source code or build outputs
- The environment forbids third-party scanning tools

[SAFETY]
- Avoid uploading proprietary code to external services without approval.
- Require review before enabling auto-fix or blocking releases.
</constraints>

<format>
Output clear and concise markdown.
</format>

