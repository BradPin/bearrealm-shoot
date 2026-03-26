---
description: "/plan-card [source]: Create issue cards from an approved plan or design document."
---

# Plan Card Workflow

## Trigger
User invokes `/plan-card [source]`.

`[source]` is optional and determines the input:
- **省略**: Read the most recent PLAN document from `.agent/plans/` (standard flow after `/plan`).
- **設計文件路徑**: Read directly from a `design/` file (e.g., `/plan-card design/game/system/戰鬥系統.md`). Use this shortcut when the design is already well-structured and doesn't need a `/plan` discussion step.

## 1. Source Reading
*   **If from PLAN**: Read `.agent/plans/PLAN-<latest>.md`, extract the Task List.
*   **If from design file**: Read the file, identify discrete implementable tasks. Activate **Game Designer** skill if needed to decompose complex designs.

## 2. Issue Card Creation
*   **Action**: Create a markdown file for EACH task in `.agent/issues/todo/`.
*   **Naming**: `ISSUE-<流水號>-<title>.md`.
*   **Content**:
    ```markdown
    ---
    id: ISSUE-[ID]
    title: [Title]
    status: todo
    source: [PLAN-ID or design file path]
    ---
    # [Title]
    
    ## Description
    [Detailed technical description]
    
    ## Required Skills
    [Which skills will be involved]
    
    ## Acceptance Criteria
    - [ ] [Criteria 1]
    - [ ] [Criteria 2]
    ```

## 3. 🚧 Review (GATE — 等待 User 審核)
*   **Present**: List all created cards with a brief summary of each.
*   **Discuss**: Refine cards if the User provides feedback. This stage may take several rounds.
*   **Wait**: Do NOT start implementation. User must explicitly invoke `/feature-start ISSUE-<num>` to begin work on a specific card.

## 4. Finalization
*   Once User approves all cards, they can invoke `/finish` to commit the planning documents.
