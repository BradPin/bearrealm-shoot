---
description: Standard workflow for implementing code features in Godot.
---

# Development Cycle Workflow

## 1. Pick & Branch
*   **Select Issue**: Choose a `TODO` task from `.agent/issues/`.
*   **Create Branch**: 
    ```bash
    git checkout -b [ID]/[ShortDescription]
    ```

## 2. Implementation Loop
*   **Understand**: Read the Issue description and acceptance criteria.
*   **Plan**: Briefly outline your changes if complex.
*   **Code**: Modify `.gd` scripts, `.tscn` files, or other resources.
*   **Test**: 
    *   Use `godot --headless --script [test_script.gd]` if unit tests exist.
    *   Or ask the User to verify manually if visual/interactive.

## 3. Review & Verification
*   **Self-Correction**: Ensure no lint errors or obvious bugs.
*   **Status Update**: Change the Issue status from `TODO` to `IN_PROGRESS`.
*   **Notify User**: 
    *   Summarize changes.
    *   Explicitly ask: "I have implemented the changes. Please verify. If approved, I will mark the issue as DONE and commit."
    *   **STOP**: Do NOT commit yet. Wait for User feedback.

## 4. Finalize & Commit
*   **Action**: Only AFTER User approval:
    1.  **Update Issue**: Change status to `DONE`.
    2.  **Commit**: (Follow `<type>(<scope>): <subject>` format)
        ```bash
        git add .
        git commit -m "feat(gameplay): [ID] implement jump mechanic"
        ```
    3.  **Handover**: Ask User to merge.
