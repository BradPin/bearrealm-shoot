# Bearrealm Shoot - Authority Rules & Standards (SSOT)

> **MANDATORY READING FOR ALL AGENTS.** This file is the single source of truth for all behavioral, technical, and architectural standards.

---

## 🚀 1. Token Usage & Efficiency (Critical)
*   **Lazy Loading**: NEVER read raw `.tscn`, `.tres`, or large binary/text files unless specifically instructed for raw data analysis.
*   **Tool-First Discovery**: ALWAYS use `godot-mcp` tools (e.g., `godot:get_scene_tree`) to understand scene structure.
*   **On-Demand Reference**: Only read documentation from `design/` when actively implementing a feature related to that design.
*   **Index Usage**: Use `.agent/godot_index.md` for project settings, layers, and input maps.

## 🛠️ 2. Development Standards
*   **External Services**: 
    *   **ComfyUI/AI Factory**: Managed externally by User. NEVER run `start_comfy.ps1`.
    *   **MCP Connectivity**: Assume all MCP servers in `mcp.json` are pre-configured and active.
*   **Typed GDScript**: All scripts MUST use explicit static typing for variables, parameters, and return values (e.g., `var velocity: Vector2 = Vector2.ZERO`).
*   **Godot 4.4+**: Follow modern Godot 4.4 best practices (Typed arrays, class_name, connect() syntax).
*   **Naming**: `snake_case` for files/folders/variables, `PascalCase` for classes.
*   **Automated Sync**: After modifying `project.godot`, ALWAYS run `python tools/sync_context.py`.

## 📂 3. Architectural Logic
*   **`.agent/`**: Technical state, tasks, and core rules. (Godot Ignored)
*   **`design/`**: High-level visual vibe and structured game design. (Godot Ignored)
*   **`design/raw/`**: User's original ideas. Source of truth for all game design.
*   **`tools/`**: Automation and production pipelines.

## 🧠 4. Skill Dispatcher (Hierarchical & On-Demand)
Identify and read the relevant skill level before execution. Use **Drill-down** for specialized tasks:
- **`project_management`**: Global state & Task management.
- **`art_director`**: Asset pipeline & Art style.
- **`audio_designer`**: AudioStreamPlayer management, bus routing & audio generation.
- **`ui_designer`**: Control node layouts, Theme/StyleBox tuning & responsive design.
- **`animator`**: AnimationPlayer keyframing, Tween logic & state transitions.
- **`developer` (Parent)**: Architecture & Generic coding rules.
    - **`developer/physics/`**: Physics, Vector math, Bounce logic. (Drill-down only for physics tasks)
    - **`developer/vfx/`**: GPUParticles2D, Shader scripting. (Drill-down only for visual polishing)
- **`documenter`**: Design synthesis from `raw/`.

## 🤖 5. Interaction Protocols
*   **Task-Driven**: Check `.agent/issues/in_progress` before starting work.
*   **Concise Output**: Minimize conversational filler. Provide technical solutions directly.
*   **Validation**: Every implementation must include a testing strategy (via `tests/` or manual verification scripts).
