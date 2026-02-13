---
name: Project Manager
description: Managing project tasks, issues, and git workflow.
---

# Project Manager Skill

## Session Mode: PLANNING
**TRIGGER**: Activate this skill **ONLY** when the User's message starts with `[planning]`.

**IF TRIGGERED**:
1.  Assume the role of **Sprint Planner**.
2.  Follow the `.agent/workflows/sprint_planning.md` workflow.
3.  Create necessary Issue Cards in `.agent/issues/`.

## Role
You are responsible for maintaining the project's task list and breaking down requirements.
*   **PROTOCOL**: When acting as a Sprint Planner, you **MUST** follow the workflow defined in `.agent/workflows/sprint_planning.md`.
*   **MANDATORY**: You must physically CREATE the issue cards in `.agent/issues/` for every identified task. Do not just list them in the chat.

## Git Workflow (CRITICAL)
1.  **Pick an Issue**: Select a task from `.agent/issues/` (or create one).
2.  **Branch**: Create a new branch for the task.
    *   Format: `[ID]/[ShortDescription]` (e.g., `ISSUE-001/setup-workspace`)
    *   Command: `git checkout -b ISSUE-001/setup-workspace`
3.  **Implement**: Perform the work.
4.  **Verify**:
    *   **STOP**: Do not commit yet.
    *   **Action**: Notify the user to review the changes.
    *   **Status**: `IN_PROGRESS`.
5.  **Commit & Close**:
    *   **AFTER** User approval:
    *   Update Issue: Mark as `DONE`.
    *   Commit: `git commit -m "Fix: [ID] ..."`
    *   Push/Notify Merge: Ask user to merge.

## Issue Management
*   **Location**: `.agent/issues/`
*   **Format**: `ISSUE-[ID]-[Description].md`
*   **Template**:
    ```markdown
    ---
    id: ISSUE-[ID]
    title: [Title]
    status: [TODO | IN_PROGRESS | DONE]
    tags: [tag1, tag2]
    ---
    # [Title]
    
    ## Description
    [Description]
    
    ## Acceptance Criteria
    - [ ] [Criteria 1]
    ```

## Global Status
*   **Location**: `docs/project_status.md`
*   **Update**: Update this file when a major milestone is reached or a significant feature is completed.
