# Developer Skill: Technical Architect (Parent)

## 🎯 總體職責
- 維護代碼結構與 Typed GDScript 規範。
- 確保所有功能符合 `.agent/rules.md`。
- **路由 (Routing)**: 根據任務深度，下鑽到專精子技能。

## 🛠️ 下鑽子技能目錄 (Drill-down)
If the task requires specialized knowledge, READ the corresponding sub-skill:
- **`./physics/SKILL.md`**: Physics, Vector math, Bounce logic.
- **`./vfx/SKILL.md`**: GPUParticles2D, AnimationPlayer, Squash & Stretch.

## 🔑 核心通用規範
- **Typed Everything**: 強制強型別。
- **Scene Access**: 優先調用 `godot-mcp` 讀取場景樹。
- **Signals**: 統一使用 Godot 4 `target.signal.connect(callable)`。
