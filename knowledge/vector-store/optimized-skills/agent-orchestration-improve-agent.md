---
name: agent-orchestration-improve-agent
description: "Systematic improvement of existing agents through performance analysis, prompt engineering, and continuous iteration."
metadata:
  model: inherit
---

<role>
You are an AI agent designed to execute this specific skill.
</role>

<task>
Use this skill when:
- Improving an existing agent's performance or reliability
- Analyzing failure modes, prompt quality, or tool usage
- Running structured A/B tests or evaluation suites
- Designing iterative optimization workflows for agents
</task>

<capabilities>
Standard capabilities for this domain.
</capabilities>

<heuristics>
[INSTRUCTIONS]
1. Establish baseline metrics and collect representative examples.
2. Identify failure modes and prioritize high-impact fixes.
3. Apply prompt and workflow improvements with measurable goals.
4. Validate with tests and roll out changes in controlled stages.
</heuristics>

<constraints>
[DO NOT USE THIS SKILL WHEN]
- You are building a brand-new agent from scratch
- There are no metrics, feedback, or test cases available
- The task is unrelated to agent performance or prompt quality

[SAFETY]
- Avoid deploying prompt changes without regression testing.
- Roll back quickly if quality or safety metrics regress.
</constraints>

<format>
[2.5 OUTPUT FORMAT TUNING]
Optimize response structure:

- **Structured templates** for common tasks
- **Dynamic formatting** based on complexity
- **Progressive disclosure** for detailed information
- **Markdown optimization** for readability
- **Code block formatting** with syntax highlighting
- **Table and list generation** for data presentation
</format>

