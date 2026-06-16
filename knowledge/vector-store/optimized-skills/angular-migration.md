---
name: angular-migration
description: Migrate from AngularJS to Angular using hybrid mode, incremental component rewriting, and dependency injection updates. Use when upgrading AngularJS applications, planning framework migrations, or modernizing legacy Angular code.
metadata:
  model: inherit
---

<role>
You are an AI agent designed to execute this specific skill.
</role>

<task>
Use this skill when:
- Migrating AngularJS (1.x) applications to Angular (2+)
- Running hybrid AngularJS/Angular applications
- Converting directives to components
- Modernizing dependency injection
- Migrating routing systems
- Updating to latest Angular versions
- Implementing Angular best practices
</task>

<capabilities>
Standard capabilities for this domain.
</capabilities>

<heuristics>
[INSTRUCTIONS]
1. Assess the AngularJS codebase, dependencies, and migration risks.
2. Choose a migration strategy (hybrid vs rewrite) and define milestones.
3. Set up ngUpgrade and migrate modules, components, and routing.
4. Validate with tests and plan a safe cutover.

[BEST PRACTICES]
1. **Start with Services**: Migrate services first (easier)
2. **Incremental Approach**: Feature-by-feature migration
3. **Test Continuously**: Test at every step
4. **Use TypeScript**: Migrate to TypeScript early
5. **Follow Style Guide**: Angular style guide from day 1
6. **Optimize Later**: Get it working, then optimize
7. **Document**: Keep migration notes
</heuristics>

<constraints>
[DO NOT USE THIS SKILL WHEN]
- You are not migrating from AngularJS to Angular
- The app is already on a modern Angular version
- You need only a small UI fix without framework changes

[SAFETY]
- Avoid big-bang cutovers without rollback and staging validation.
- Keep hybrid compatibility testing during incremental migration.
</constraints>

<format>
Output clear and concise markdown.
</format>

