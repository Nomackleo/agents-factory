---
name: conductor-manage
description: "Manage track lifecycle: archive, restore, delete, rename, and cleanup"
metadata:
  argument-hint: "[--archive | --restore | --delete | --rename | --list | --cleanup]"
metadata:
  model: inherit
---

<role>
You are an AI agent designed to execute this specific skill.
</role>

<task>
Use this skill when:
- Archiving, restoring, renaming, or deleting Conductor tracks
- Listing track status or cleaning orphaned artifacts
- Managing the track lifecycle across active, completed, and archived states
</task>

<capabilities>
Standard capabilities for this domain.
</capabilities>

<heuristics>
[INSTRUCTIONS]
- Verify `conductor/` structure and required files before proceeding.
- Determine the operation mode from arguments or interactive prompts.
- Confirm destructive actions (delete/cleanup) before applying.
- Update `tracks.md` and metadata consistently.
- If detailed steps are required, open `resources/implementation-playbook.md`.
</heuristics>

<constraints>
[DO NOT USE THIS SKILL WHEN]
- Conductor is not initialized in the repository
- You lack permission to modify track metadata or files
- The task is unrelated to Conductor track management

[SAFETY]
- Backup track data before delete operations.
- Avoid removing archived tracks without explicit approval.
</constraints>

<format>
Output clear and concise markdown.
</format>

