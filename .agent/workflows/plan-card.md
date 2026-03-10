---
description: "/plan-card: After plan approval, convert the plan tasks into individual issue cards."
---

# Plan Card Workflow

## Trigger
User requests to enter card creation phase with `/plan-card`.

## 1. Issue Card Creation
*   **Action**: Create a markdown file for EACH task in `.agent/issues/todo/`.
*   **Naming**: `ISSUE-<流水號>-<title>.md`.
*   **Content**:
    - **ID**: `ISSUE-[SequentialID]`
    - **Title**: Clear and concise.
    - **Status**: `todo`
    - **Description**: Detailed implementation guide.
    - **Acceptance Criteria**: Checklist for completion.

## 2. Iteration
*   **Review**: Present the list of created cards to the User.
*   **Discuss**: Refine cards if the User provides feedback. This stage may take several rounds.
