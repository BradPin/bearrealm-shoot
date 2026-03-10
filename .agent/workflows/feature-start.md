---
description: "/feature-start ISSUE-<num>: Start implementation of a specific issue."
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
*   **Update**: Ensure the internal status in the markdown frontmatter is also updated if applicable.

## 3. Implementation
*   **Action**: Begin working on the task following the issue description.
