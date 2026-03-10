---
name: Project Manager
description: Managing project tasks, issues, and git workflow.
---

# Project Manager Skill

## Session Mode: PLANNING
**TRIGGER**: Activate this skill when the User uses `/plan`, `/plan-card`, or `/plan-finish`.

**TASKS**:
1.  **Plan Logic**: Follow `.agent/workflows/plan.md` to create planning documents in `.agent/plans/`.
2.  **Card Logic**: Follow `.agent/workflows/plan-card.md` to create issue cards in `.agent/issues/todo/`.
3.  **Finish Logic**: Follow `.agent/workflows/plan-finish.md` to commit and finalize planning.

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
*   **Update**: Keep `docs/project_status.md` updated with high-level progress.
