---
description: "/finish: Finalize the current phase — auto-detects context from git branch, commits changes."
---

# Finish Workflow (統一收尾)

## Trigger
User invokes `/finish` to close the current working phase.

## 1. Context Detection (自動偵測)
Determine the current phase by checking the **git branch name**:

| Branch Pattern | Detected Phase | Behavior |
|---------------|----------------|----------|
| `PLAN-*` | 📋 Planning | Commit planning docs |
| `ISSUE-*` | ⚙️ Feature | Move card to done, commit implementation |
| Any (after `review-context`) | 🧹 Review | Commit context changes |

If ambiguous, ask User to clarify: `/finish plan`, `/finish feature`, or `/finish review`.

---

## 2. Phase-Specific Actions

### 📋 Planning Finish
1. **Commit**: Organize commits by theme.
   - Format: `docs(planning): [PLAN-ID] [Description]`
2. **Notify**: Inform User that planning is closed and ISSUE cards are ready in `todo/`.

### ⚙️ Feature Finish
1. **Card Management**:
   - Move ISSUE card from `.agent/issues/in_progress/` to `.agent/issues/done/`.
   - Update frontmatter status to `done`.
2. **Commit**: Organize commits by logical groups (UI, logic, assets, etc.).
   - Format: `feat/fix/refactor: [ISSUE-ID] [Description]`
   - Each commit = one cohesive change.
3. **Notify**: Inform User the feature is done and card is moved.

### 🧹 Review Finish
1. **Commit**: Commit all context changes made during the review.
   - Format: `chore(context): review-context audit [DATE]`
2. **Notify**: Present a summary of what was cleaned up.

---

## 3. Common Rules (所有 phase 共用)
- **Logical Groups**: Never cram unrelated changes into one commit.
- **No Secrets**: Do not commit `.env`, credentials, or API keys.
- **Branch Awareness**: Commit on the current working branch, do NOT merge to main.
- **User Confirmation**: If there are unstaged changes that look unrelated to the current phase, ask User before including them.
