---
description: "review-context: Audit and optimize the Agent context system for accuracy and token efficiency."
---

# Review-Context Workflow (Context 架構審查)

## Trigger
User invokes `review-context` or Agent proactively suggests after 3+ feature completions.

## Execution Steps

### Step 1: Inventory Scan (盤點)
Collect a full inventory of the context system:
```
Scan targets:
├── .cursorrules, GEMINI.md           (entry points)
├── .agent/rules.md                    (SSOT)
├── .agent/overview.md                 (status)
├── .agent/guidelines.md               (standards)
├── .agent/skills/**/SKILL.md          (all skills)
├── .agent/workflows/*.md              (all workflows)
├── .agent/protocols/*.md              (all protocols)
└── .agent/design/vibe/*.md            (prompt vaults)
```

For each file, record:
- **Line count** (proxy for token weight)
- **Last meaningful update** (via git log)
- **Referenced paths** (extract all relative paths)

### Step 2: Path Verification (路徑驗證)
For every path reference found in Step 1:
1. Verify the target file/directory exists.
2. If NOT: flag as `PHANTOM` and auto-fix if an obvious correct path exists.
3. If AMBIGUOUS: flag as `NEEDS_DECISION` and present options to User.

### Step 3: Conflict Detection (衝突偵測)
Cross-reference key definitions:
- **Style keywords**: Compare `design/vibe.md` ↔ `master_art_prompt.md` for consistency.
- **Naming rules**: Compare `rules.md` ↔ `guidelines.md` for contradictions.
- **Skill boundaries**: Check for overlapping responsibilities between Skills.
- **Workflow gaps**: Ensure every Skill referenced in `rules.md` has a corresponding `SKILL.md`.

### Step 4: Error Pattern Mining (錯誤模式挖掘)
```bash
git log --oneline -20    # Recent commits
git diff HEAD~10 --stat  # Recent file changes
```
Analyze for patterns:
- Repeated path corrections → missing rule
- Repeated type errors → missing guideline
- Repeated MCP parameter mistakes → outdated prompt vault

Distill findings into **new concise rules** and append to appropriate files.

### Step 5: Token Optimization (Token 瘦身)
Identify and propose removal/archival of:
- Files not referenced by any active Skill or Workflow.
- Verbose descriptions that can be compressed without losing meaning.
- Legacy documents (e.g., setup guides) that served their purpose.

### Step 6: Apply & Report (套用與報告)
1. Auto-apply safe fixes (phantom paths, typos).
2. Present diff preview for SSOT changes (`rules.md`, `overview.md`).
3. Generate the Context Review Report (format defined in `context_reviewer/SKILL.md`).
4. **🚧 GATE**: Present report to User. Wait for User to invoke `/finish` to commit changes.

## Cadence Recommendation
- **Minimum**: After every PLAN cycle completion.
- **Ideal**: After every 3 ISSUE completions.
- **Maximum**: Weekly during active development.
