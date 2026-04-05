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
*   **Producer 企劃卡（如 ISSUE-008～018）**：開卡後先讀該檔 **「Agent 協作模式（硬性）」**。預設以 **問答、缺口盤點、對照 `mvp.md`** 輔助 Producer 寫 `design/game/`，**禁止未受委託即代寫定稿**；與 **game_designer** SKILL 之 **Producer 主筆模式** 一併遵守。

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
*   **Specification clarity (MUST)**: If the ISSUE card does **not** clearly define implementation details (scope, behavior, edge cases, affected systems/files, acceptance criteria), **do not** proceed with substantial implementation. Stop and **discuss with the Producer** until the approach is agreed.
*   **Action**: Execute the task following the ISSUE description and loaded skill guidelines.
*   **Collaboration**: Follow `.agent/protocols/inter_agent.md` for multi-skill coordination.
*   **Asset Creation**: If generating assets, follow `.agent/workflows/create_asset.md` SOP.

## 5. 🚧 Completion (GATE — 等待 User 驗收)
*   **Report**: When implementation is complete, present a summary of what was done.
*   **No commit from this workflow**: Task completion **must not** include `git commit`. Commits are handled only via **`/finish`** (after Producer verification, e.g. `/feature-valid`). Do **not** commit on your own initiative at phase end.
*   **Wait**: Do NOT finalize. User should invoke `/feature-valid` to verify, then `/finish` to close.
