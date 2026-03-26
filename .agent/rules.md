# Bearrealm Shoot - Authority Rules & Standards (SSOT)

> **MANDATORY READING FOR ALL AGENTS.** Single source of truth for all behavioral, technical, and architectural standards.

---

## 🚀 1. Token Usage & Efficiency (Critical)
*   **Lazy Loading**: NEVER read raw `.tscn`, `.tres`, or large binary/text files unless specifically instructed.
*   **Tool-First Discovery**: ALWAYS use `godot` MCP tools to understand scene structure.
*   **On-Demand Reference**: Only read `design/` docs when actively implementing that content.
*   **Skill Lazy-Load**: Only read a `SKILL.md` when the current task requires that skill's domain.
*   **Index Usage**: Use `.agent/godot_index.md` for project settings, layers, and input maps.

## 🛠️ 2. Development Standards
*   **External Services**: 
    *   **ComfyUI/AI Factory**: Managed externally by User. NEVER run `start_comfy.ps1`.
    *   **MCP Connectivity**: Assume all MCP servers in `mcp.json` are pre-configured and active.
*   **Typed GDScript**: All scripts MUST use explicit static typing (see `.agent/guidelines.md`).
*   **Godot 4.4+**: Follow modern Godot 4.4 best practices (Typed arrays, class_name, connect() syntax).
*   **Naming**: `snake_case` for files/folders/variables, `PascalCase` for classes.
*   **Automated Sync**: After modifying `project.godot`, ALWAYS run `python tools/sync_context.py`.

## 📂 3. Architectural Logic (資料夾角色定義)

| 目錄 | 擁有者 | Godot 可見 | 用途 |
|------|--------|-----------|------|
| **`design/`** | **User (Producer)** | ❌ Ignored | User 親筆撰寫的設計文件、世界觀、vibe 定義。Agent 視為**唯讀輸入源**。 |
| **`design/game/`** | User + Game Designer | ❌ Ignored | 結構化企劃：系統設計、實體表、Feature Spec。Agent 可協助整理但 User 有最終審核權。 |
| **`assets/`** | Agent (Art/Audio) | ✅ Auto-import | Agent 產出的**遊戲成品資源**（圖片、音效、UI），經處理後直接供 Godot 使用。 |
| **`.agent/`** | Agent | ❌ Ignored | Agent 的工作腦：規則、技能、Issue 卡、Workflow、Prompt Vault。 |
| **`scenes/`** | Agent (Sys Architect) | ✅ | Godot 場景檔。 |
| **`tools/`** | Shared | ❌ | 自動化腳本（Python）。 |

**關鍵原則**：`design/` = User 的創意輸入 → Agent 處理後 → `assets/` = Godot 的成品輸出。

## 🧠 4. Skill Dispatcher (Hierarchical & On-Demand)
Read the relevant `SKILL.md` from `.agent/skills/<name>/` ONLY when needed:

### Management Group
- **`project_management`**: Task lifecycle, ISSUE tracking, git workflow.
- **`game_designer`**: Creative ideation → structured specs & entity sheets.
- **`context_reviewer`**: Meta-optimization, context auditing, token budget health.

### Creative Group
- **`art_director`**: Visual asset pipeline via ComfyUI MCP.
- **`audio_designer`**: Audio asset pipeline, AudioStreamPlayer routing.
- **`ui_designer`**: Control node layouts, Theme/StyleBox, responsive design.
- **`animator`**: AnimationPlayer, Tween logic, state transitions.
- **`vfx_artist`**: GPUParticles2D, Shader scripting, visual polish.

### Engineering Group
- **`systems_architect`**: Godot node architecture, scene assembly, resource integration.
- **`developer`**: Architecture, generic coding rules, physics & vector math.

## 🔗 5. Collaboration Protocol (Human-in-the-Loop)
*   **Inter-Agent**: For multi-step tasks, follow `.agent/protocols/inter_agent.md`.
*   **Producer Control**: User 是 Producer，所有重大階段轉換需要 User 明確批准。Agent 不可自行跳過審核關卡。
*   **Artifact Handoff**: Skills communicate through concrete file artifacts, not implicit state.
*   **Gate Pattern**: 每個階段完成後，**停下來等 User 指令**，不自行推進到下一階段。

## 🤖 6. Interaction Protocols
*   **Task-Driven**: Check `.agent/issues/in_progress/` before starting work.
*   **Concise Output**: Minimize conversational filler. Provide technical solutions directly.
*   **Validation**: Every implementation must include a testing strategy.
*   **Finish**: 所有階段收尾統一用 `/finish`，自動偵測 context (see `.agent/workflows/finish.md`)。
*   **Maintenance**: Periodically run `review-context` workflow (see `.agent/workflows/review-context.md`).
