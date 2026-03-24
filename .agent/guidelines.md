# Godot 4.4+ GDScript 寫作規範

> 為了提升代碼可靠性與 AI 的理解能力，本專案強制執行以下規範。

## 1. 強型別標註 (Strict Typing)
所有變數、常數與函數必須明確標註類型。

*   **變數宣告**: `var velocity: Vector2 = Vector2.ZERO` (而非 `var velocity`)
*   **函數定義**: `func _physics_process(delta: float) -> void:` (而非 `func _physics_process(delta):`)
*   **回傳值**: 即使不回傳也應明確標註 `-> void`。

## 2. 核心架構 (Core Architecture)
*   **彈珠控制**: 優先使用 `CharacterBody2D` 搭配 `move_and_slide()`。
*   **信號模式**: 使用 Godot 4 的信號連接語法 `target.signal_name.connect(callable)`。
*   **資源引用**: 優先使用 `class_name` 定義類別，以便於在代碼中進行類型檢查 (`if obj is Marble:`)。

## 3. 命名規範 (Naming Convention)
*   **檔案/目錄**: `snake_case` (例如：`player_marble.tscn`)
*   **類別名稱**: `PascalCase` (例如：`class_name PlayerMarble`)
*   **變數/函數**: `snake_case`
*   **私有成員**: 前綴底線 `_private_method()`

## 4. 碰撞層級定義 (Collision Layers)
依據 `project.godot` 定義進行操作，避免在代碼中使用硬編碼的 Layer ID。

## 5. 註解規範
每個類別上方應簡述其職責，重要屬性應加上 `@export_group` 與註解，方便在 Inspector 中調整企劃數值。
