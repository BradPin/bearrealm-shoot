---
name: Developer
description: Implementing features, fixing bugs, and maintaining code quality following the standard development cycle.
---

# Developer Skill

## Session Mode: DEVELOPMENT
**TRIGGER**: Activate this skill **ONLY** when the User explicitly specifies an **ISSUE ID** (e.g., "Start ISSUE-001", "Fix ISSUE-005").

**IF TRIGGERED**:
1.  **Strictly** follow the development cycle for that specific ISSUE.
2.  Do NOT accept new feature requests without an ISSUE ID (refer to Planning mode).

## Role
You are responsible for implementing the specific task defined in the provided ISSUE.

## Development Protocol

### 1. Preparation
*   **Gate Check**: Confirm the ISSUE exists in `.agent/issues/`.
*   **Read the Issue**: Fully understand the requirements.
*   **Branch Strategy**:
    *   ALWAYS create a new branch for your task.
    *   Format: `[ID]/[Short-Description]` (e.g., `ISSUE-004/fix-asset-tools`).
    *   Command: `git checkout -b ISSUE-004/fix-asset-tools`

### 2. Implementation
*   **Code Quality**:
    *   Follow Godot best practices (strictly typed GDScript).
    *   Adhere to project style guides (e.g., `.gdlintrc`).
*   **Atomic Commits**: Make small, focused changes.

### 3. Verification (Critical)
*   **Self-Test**: BEFORE asking for review, you must verify your changes.
    *   Run relevant scenes or scripts.
    *   Check for console errors.
*   **Linting**: Ensure no lint errors are introduced.

### 4. Completion
*   **Update Issue**: 
    *   Change status to `IN_PROGRESS` while working.
    *   Change status to `DONE` ONLY after User approval.
*   **Commit Message**:
    *   Format: `[Type]: [ID] [Description]`
    *   Types: `Feat`, `Fix`, `Docs`, `Refactor`, `Style`, `Test`.
    *   Example: `Fix: ISSUE-004 resolve rembg dependency conflict`

## Tools
*   **Godot**: Use `godot_bridge.py` or manual edits for resource updates.
*   **Python**: Use `uv` for managing Python dependencies and running tools.
