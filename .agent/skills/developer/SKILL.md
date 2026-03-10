---
name: Developer
description: Implementing features, fixing bugs, and maintaining code quality following the standard development cycle.
---

# Developer Skill

## Session Mode: DEVELOPMENT
**TRIGGER**: Activate this skill when the User uses `/feature-start`, `/feature-valid`, or `/feature-finish`.

**TASKS**:
1.  **Start Logic**: Follow `.agent/workflows/feature-start.md` to begin implementation.
2.  **Valid Logic**: Follow `.agent/workflows/feature-valid.md` to verify changes.
3.  **Finish Logic**: Follow `.agent/workflows/feature-finish.md` to finalize and commit.

## Role
You are responsible for implementing the specific task defined in the provided ISSUE card.

## Development Protocol

### 1. Preparation
*   **Gate Check**: Confirm the ISSUE exists in `.agent/issues/todo/` or `.agent/issues/in_progress/`.
*   **Branching**: `ISSUE-<num>/<title>`

### 2. Implementation
*   **Code Quality**: Godot best practices, strictly typed GDScript.
*   **Card Migration**: Move card to `in_progress` when starting.

### 3. Verification
*   **Self-Correction**: Run tests, check for console errors, ensure linting passes.
*   **Command**: `/feature-valid` to summarize verification for user.

### 4. Completion
*   **Approval**: Only finalize AFTER the user confirms.
*   **Commit Format**: `type: [ID] [Description]` (e.g., `feat: ISSUE-001 implement jump`)
*   **Logical Groups**: Organize implementation into thematic commits.

## Tools
*   **Godot**: Use `godot_bridge.py` or manual edits.
*   **Python**: Use `uv` for dependencies.
