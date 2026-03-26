---
description: "/feature-start ISSUE-<num>: Start implementation of a specific issue card."
---

# Feature Start Workflow

## Trigger
User initiates implementation with `/feature-start ISSUE-<num>`.

## 1. Branching
*   **Action**: Checkout to a new branch for the issue.
*   **Format**: `ISSUE-<num>/<title>`
*   **Command**: `git checkout -b ISSUE-<num>/[title]`

## 2. Card Management
*   **Action**: Move the issue card from `.agent/issues/todo/` to `.agent/issues/in_progress/`.
*   **Update**: Change the frontmatter status to `in_progress`.

## 3. Skill Dispatch
Read the ISSUE card's **Required Skills** field and load ONLY those skills:
*   需要美術？→ Read `art_director/SKILL.md`, follow `create_asset.md` workflow.
*   需要音效？→ Read `audio_designer/SKILL.md`.
*   需要特效？→ Read `vfx_artist/SKILL.md`.
*   需要場景組裝？→ Read `systems_architect/SKILL.md`.
*   需要寫程式？→ Read `developer/SKILL.md`.
*   需要動畫？→ Read `animator/SKILL.md`.
*   需要 UI？→ Read `ui_designer/SKILL.md`.

Only load skills that are actually needed. Do NOT load all skills.

## 4. Implementation
*   **Action**: Execute the task following the ISSUE description and loaded skill guidelines.
*   **Collaboration**: Follow `.agent/protocols/inter_agent.md` for multi-skill coordination.
*   **Asset Creation**: If generating assets, follow `.agent/workflows/create_asset.md` SOP.

## 5. 🚧 Completion (GATE — 等待 User 驗收)
*   **Report**: When implementation is complete, present a summary of what was done.
*   **Wait**: Do NOT finalize. User should invoke `/feature-valid` to verify, then `/finish` to close.
