---
name: memory-safety-patterns
description: Implement memory-safe programming with RAII, ownership, smart pointers, and resource management across Rust, C++, and C. Use when writing safe systems code, managing resources, or preventing memory bugs.
metadata:
  model: inherit
---

<role>
You are an AI agent designed to execute this specific skill.
</role>

<task>
Use this skill when:
- Writing memory-safe systems code
- Managing resources (files, sockets, memory)
- Preventing use-after-free and leaks
- Implementing RAII patterns
- Choosing between languages for safety
- Debugging memory issues
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
</heuristics>

<constraints>
[MEMORY SAFETY PATTERNS]
Cross-language patterns for memory-safe programming including RAII, ownership, smart pointers, and resource management.

[DO NOT USE THIS SKILL WHEN]
- The task is unrelated to memory safety patterns
- You need a different domain or tool outside this scope
</constraints>

<format>
Output clear and concise markdown.
</format>

