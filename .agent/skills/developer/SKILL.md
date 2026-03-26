# Developer Skill (開發者)

## 🎯 職責
- 維護代碼結構與 Typed GDScript 規範。
- 實作遊戲邏輯、系統架構、物理機制。
- 確保所有功能符合 `.agent/rules.md` 與 `.agent/guidelines.md`。

## 🔑 核心規範
- **Typed Everything**: 所有變數、參數、回傳值強制標註類型。
- **Scene Access**: 優先調用 `godot` MCP 工具讀取場景樹，不讀取原始 `.tscn`。
- **Signals**: 統一使用 Godot 4 `target.signal.connect(callable)`。
- **class_name**: 所有自定義腳本必須定義 `class_name`，啟用類型安全引用。
- **@export**: 企劃可調參數使用 `@export var`，搭配 `@export_group()` 分組。

## 🎯 物理 & 向量數學 (Physics Specialization)
本專案核心玩法為彈珠碰撞，以下為物理相關的關鍵規範：
- **彈珠反彈**: 實作基於 `CharacterBody2D` + `move_and_slide()` 的精確向量反彈。
- **Bounce**: 優先使用 `velocity.bounce(normal)`。
- **動量計算**: 處理碰撞後的能量傳遞與衰減。
- **預測線 (Trajectory)**: 計算物理路徑的視覺化投射。
- 所有物理參數必須定義為 `@export var`，方便企劃調整。
- 嚴格依照 `.agent/godot_index.md` 的 `collision_layer` 與 `collision_mask` 定義。

## 🧩 協作
- **From Systems Architect**: 接收場景節點架構，在正確位置掛載腳本。
- **From Game Designer**: 接收 Feature Spec 中的技術需求。
- **To Animator / VFX Artist**: 提供信號觸發點 (signal) 以便掛接動畫與特效。
