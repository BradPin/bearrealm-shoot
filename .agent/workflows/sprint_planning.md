---
description: Sprint planning workflow for breaking down requirements into tasks.
---

# Sprint Planning Workflow

## Trigger
User initiates a planning session or provides high-level requirements (e.g., "I want a new enemy type").

## 1. Analysis & Discussion
*   **Discuss**: Clarify requirements with the User until a clear picture is formed.
*   **Scope**: Identify the boundaries of the work.

## 2. Task Breakdown (PM Mode)
*   **Structure**: Break the requirement into hierarchical tasks:
    *   **Epic**: Large feature (e.g., "New Enemy System").
    *   **Story**: User-facing functionality (e.g., "Enemy Chase Logic").
    *   **Task**: Specific technical implementation (e.g., "Implement A* Pathfinding script").
*   **Granularity**: Each Task should be small enough to complete in a single session (1-2 hours).
*   **Relationships**: Note parent/child relationships in the task description.

## 3. Card Creation
*   **Action**: Create a markdown file for EACH task in `.agent/issues/`.
*   **Naming**: `ISSUE-[SequentialID]-[ShortDesc].md`.
*   **Content**:
    - **ID**: Unique identifier.
    - **Title**: Clear and concise.
    - **Status**: `TODO`.
    - **Parent**: Reference the Epic/Story ID (if applicable).
    - **Description**: Detailed implementation guide.
    - **Acceptance Criteria**: Checklist for completion.

## 4. Confirmation & Commit
*   **Review**: Present the list of created tasks to the User.
*   **Wait for Approval**: Ask the User if the plan looks correct.
*   **Commit**: Once approved, commit the new issue cards.
    *   **Format**: `<type>(<scope>): <subject>` (e.g., `docs(planning): create sprint backlog`)
    *   **Command**: `git add .agent/issues/`, `git commit -m "docs(planning): add [ID] to [ID] sprint tasks"`
*   **Prioritize**: Ask the User which task to start first.
