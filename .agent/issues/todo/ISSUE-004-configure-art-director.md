---
id: ISSUE-004
title: Configure Art Director Skill
status: TODO
tags: [skills, agent, configuration]
---
# Configure Art Director Skill

## Description
Update the `Art Director` skill to fully utilize the new art direction guidelines and generation tools.

## Context
The `.agent/skills/art_director/SKILL.md` needs to be the authoritative source for how the agent acts as an Art Director. It must reference the new tools and vibe documentation.

## Tasks
1.  Update `.agent/skills/art_director/SKILL.md`.
2.  Add specific workflows for:
    - "New Icon Request" -> `tools/generate_icon.py`.
    - "Vibe Check" -> Comparisons with `design/art/vibe`.
3.  Define standard prompt templates within the skill for fallback.

## Acceptance Criteria
- [ ] `.agent/skills/art_director/SKILL.md` is updated.
- [ ] The skill explicitly references `docs/project_vibe.md`.
- [ ] The skill includes instructions on using `tools/generate_icon.py`.
