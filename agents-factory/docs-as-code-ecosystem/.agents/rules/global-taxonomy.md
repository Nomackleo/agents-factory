# Global Taxonomy and Naming Conventions

> [!IMPORTANT]
> ALL agents operating within the Docs-as-Code Ecosystem MUST adhere strictly to these taxonomies. Failure to do so is considered a critical error in documentation quality.

## Naming Conventions
- **Files and Directories**: STRICT `kebab-case`. Absolutely no spaces, underscores, or CamelCase allowed.
  - *Correct*: `platform-architecture-design.md`
  - *Incorrect*: `Platform_Architecture_Design.md` or `platformArchitectureDesign.md`
- **Dates**: Strict ISO 8601 format (`YYYY-MM-DD`).
- **Enumerations**: Must always include leading zeros for sorting consistency (e.g., `0001`, `0002`, `0010`).

## Document Context Rule (The 5 W's)
To mitigate the "curse of knowledge," **every single document** generated in this ecosystem MUST explicitly answer the five fundamental questions (WHO, WHAT, WHEN, WHERE, WHY) in its first two paragraphs.

1. **WHO**: Who is the primary audience and who owns this document/system?
2. **WHAT**: What is the system/process/architecture being described?
3. **WHEN**: When was this decision made or when does this process apply?
4. **WHERE**: Where does this system live (repository, cloud environment, domain)?
5. **WHY**: Why does this exist? What is the core business or technical problem it solves?

## ISO and Security Standards
- Apply ISO 25010 (Quality), 42001 (AI), 27001 (Security) and SOC 2 principles implicitly in the documentation without explicitly citing the standard names unless legally required.
- Maintain maximum exegetical tone and argumentative quality.

## Metrics
- Focus on algorithmic efficiency.
- Evaluate engineering impact through DORA metrics (Deployment Frequency, Lead Time for Changes, Change Failure Rate, Time to Restore Service).
- Evaluate developer experience through SPACE framework (Satisfaction, Performance, Activity, Communication, Efficiency).
