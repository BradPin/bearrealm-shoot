---
name: Project Manager
description: Managing project tasks, issues, and git workflow.
---

# Project Manager Skill

## Workflow Triggers
**TRIGGER**: Activate this skill when the User uses any of these workflow commands:

| 指令 | Workflow | 動作 |
|------|----------|------|
| `/plan <input>` | `workflows/plan.md` | 討論需求、產出 PLAN 文件 |
| `/plan-card [source]` | `workflows/plan-card.md` | 從 PLAN 或設計文件拆出 ISSUE 卡 |
| `/feature-start ISSUE-N` | `workflows/feature-start.md` | 建分支、搬卡、調度 Skill 實作 |
| `/feature-valid` | `workflows/feature-valid.md` | 驗證實作結果 |
| `/finish` | `workflows/finish.md` | 收尾當前階段 (auto-detect context) |

## Role
You are responsible for maintaining the project's task list, architectural plans, and breaking down requirements.
*   **PROTOCOL**: Always follow the specific workflow associated with the slash command used.
*   **MANDATORY**: PHYSICALLY create the files (plans and issues) in their respective directories.

## Git Workflow
1.  **Planning Branch**: `PLAN-<ID>/<title>`
2.  **Commit Standards**: Organize commits by theme. Use `docs(planning): [ID] description`.

## Issue Management
*   **Structure**: 
    - `.agent/issues/todo/`: Upcoming tasks.
    - `.agent/issues/in_progress/`: Currently active tasks.
    - `.agent/issues/done/`: Completed tasks.
*   **Template**:
    ```markdown
    ---
    id: ISSUE-[ID]
    title: [Title]
    status: [todo | in_progress | done]
    ---
    # [Title]
    
    ## Description
    [Detailed technical description]
    
    ## Acceptance Criteria
    - [ ] [Criteria]
    ```

## Project Status
*   **Update**: Keep `.agent/overview.md` updated with high-level progress and current focus.
