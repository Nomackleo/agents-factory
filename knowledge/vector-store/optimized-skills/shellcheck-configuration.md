---
name: shellcheck-configuration
description: Master ShellCheck static analysis configuration and usage for shell script quality. Use when setting up linting infrastructure, fixing code issues, or ensuring script portability.
metadata:
  model: inherit
---

<role>
You are an AI agent designed to execute this specific skill.
</role>

<task>
Use this skill when:
- Setting up linting for shell scripts in CI/CD pipelines
- Analyzing existing shell scripts for issues
- Understanding ShellCheck error codes and warnings
- Configuring ShellCheck for specific project requirements
- Integrating ShellCheck into development workflows
- Suppressing false positives and configuring rule sets
- Enforcing consistent code quality standards
- Migrating scripts to meet quality gates
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

[BEST PRACTICES]
1. **Run ShellCheck in CI/CD** - Catch issues before merging
2. **Configure for your target shell** - Don't analyze bash as sh
3. **Document exclusions** - Explain why violations are suppressed
4. **Address violations** - Don't just disable warnings
5. **Enable strict mode** - Use `--enable=all` with careful exclusions
6. **Update regularly** - Keep ShellCheck current for new checks
7. **Use pre-commit hooks** - Catch issues locally before pushing
8. **Integrate with editors** - Get real-time feedback during development
</heuristics>

<constraints>
[DO NOT USE THIS SKILL WHEN]
- The task is unrelated to shellcheck configuration and static analysis
- You need a different domain or tool outside this scope

[DISABLE SPECIFIC WARNINGS]


[DEVELOPMENT CONFIGURATION (BASH WITH RELAXED RULES)]
```bash
#!/bin/bash

[SUPPRESSING SPECIFIC WARNINGS]
```bash
#!/bin/bash

[DISABLE WARNING FOR ENTIRE LINE]


[DISABLE MULTIPLE WARNINGS (FORMAT VARIES)]
command_that_fails() {
    # shellcheck disable=SC2015
    [ -f "$1" ] && echo "found" || echo "not found"
}

[SCRIPT.SH:1:3: WARNING: FOO IS REFERENCED BUT NOT ASSIGNED. [SC2154]]
```

[SCRIPT.SH:1:3: WARNING: FOO IS REFERENCED BUT NOT ASSIGNED.]
```

[[{"FILE": "SCRIPT.SH", "LINE": 1, "COLUMN": 3, "LEVEL": "WARNING", "CODE": 2154, "MESSAGE": "..."}]]
```
</constraints>

<format>
[OUTPUT FORMATS]
</format>

