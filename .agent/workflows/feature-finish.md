---
description: "/feature-finish: Finalize the implementation, move card to done, and commit."
---

# Feature Finish Workflow

## Trigger
Implementation is verified and ready to be closed.

## 1. Card Management
*   **Action**: Move the issue card from `.agent/issues/in_progress/` to `.agent/issues/done/`.
*   **Update**: Change the status in the frontmatter to `done`.

## 2. Commit Implementation
*   **Action**: Commit the changes.
*   **Logical Groups**: Organize commits by theme/topic (e.g., UI changes, logic changes).
*   **Commit Format**: `feat/fix/refactor: [ID] [Description]`
*   **Rule**: Ensure each commit represents a single cohesive change.

## 3. Notification
*   **Inform**: Let the user know the feature is finished and the card is moved to `done`.
