---
description: "/plan <descriptions>: Initiate planning phase by discussing requirements and creating a plan document."
---

# Plan Workflow

## Trigger
User initiates planning with `/plan <descriptions>`.

## 1. Analysis & Discussion
*   **Discuss**: Clarify the `<descriptions>` with the User. 
*   **Goal**: Reach a consensus on direction and scope.
*   **Iterate**: Ask clarifying questions and propose initial thoughts.

## 2. Plan Creation
*   **Action**: Create a markdown file in `.agent/plans/PLAN-<流水號>-<title>.md`.
*   **Content**: Outline the strategy, architecture changes, and a list of tasks.
*   **Template**:
    ```markdown
    # PLAN-[ID]: [Title]
    
    ## Objective
    [What are we trying to achieve?]
    
    ## Implementation Strategy
    [High-level technical approach]
    
    ## Task List
    - [ ] Task 1
    - [ ] Task 2
    ```

## 3. Branching
*   **Action**: Checkout to a new branch for the planning process.
*   **Format**: `PLAN-<流水號>/<title>`
*   **Command**: `git checkout -b PLAN-[ID]/[title]`

## 4. Confirmation
*   **Wait**: Present the initial plan to the User and wait for feedback or approval.
