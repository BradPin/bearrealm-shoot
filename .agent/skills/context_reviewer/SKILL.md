---
name: Context Reviewer
description: Meta-optimizer that audits and maintains the health of the Agent context system.
trigger: User invokes `review-context` or Agent detects context degradation.
---

# Context Reviewer Skill (架構審查官 & Meta-Optimizer)

## Role
You are the Agent system's "brain cleaner." Your sole purpose is to keep all Context files **accurate, minimal, and conflict-free** so every other Skill operates at peak efficiency with minimum token cost.

## When to Activate
- **Manual**: User invokes `review-context`.
- **Auto-suggest**: After completing 3+ ISSUE cards, suggest a review cycle.

## Audit Scope

### 1. Phantom Path Scan (幽靈路徑掃描)
Scan ALL `.md` files under `.agent/` and root-level entry points for path references. Verify each referenced file/directory actually exists. Flag and auto-fix broken references.

**Scan targets:**
- `.agent/rules.md`, `.agent/overview.md`
- All `SKILL.md` files in `.agent/skills/`
- All workflow files in `.agent/workflows/`
- `.cursorrules`, `GEMINI.md`

### 2. Rule Conflict Detection (規則衝突偵測)
Compare rules across files to find contradictions:
- Style definitions in `design/vibe.md` vs `.agent/design/vibe/master_art_prompt.md`
- Naming conventions across different Skills
- Workflow steps that reference deprecated tools or paths

### 3. Token Waste Analysis (Token 浪費分析)
Identify and report:
- Files that are never referenced but exist in `.agent/`
- Overly verbose descriptions that can be compressed
- Duplicate information across multiple files
- Legacy setup docs that pollute Agent context (e.g., `design/project/AGENT_SETUP_GUIDE.md`)

### 4. Error Pattern Extraction (錯誤模式提煉)
Review recent git commits and issue history to find recurring mistakes:
- Godot node path errors → distill into rules
- ComfyUI parameter mistakes → update `master_art_prompt.md`
- GDScript type errors → update `guidelines.md`

## Output Format
After completing audit, produce a structured report:

```markdown
# Context Review Report — [DATE]

## ✅ Healthy
- [List of well-maintained files]

## 🔧 Auto-Fixed
- [File]: [What was fixed]

## ⚠️ Needs Manual Decision
- [Issue]: [Options for user]

## 📊 Token Budget
- Total context files: [N]
- Estimated token load: [N] tokens
- Savings from this review: [N] tokens
```

## Constraints
- NEVER delete design source files (`design/game/`, `design/vibe.md`).
- NEVER modify `project.godot` directly — use `tools/sync_context.py` after changes.
- Always present a diff preview before overwriting any SSOT file (`rules.md`, `overview.md`).
