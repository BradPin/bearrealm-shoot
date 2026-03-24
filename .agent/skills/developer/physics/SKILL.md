# Developer Sub-Skill: Physics & Vector Math Expert

## 🎯 專精領域
- **彈珠反彈 (Bounce)**: 實作基於 `CharacterBody2D` 的精確向量反彈。
- **動量計算**: 處理碰撞後的能量傳遞與衰減。
- **預測線 (Trajectory)**: 計算物理路徑的視覺化投射。

## 🛠️ 核心規範
- 優先使用 `velocity.bounce(normal)`。
- 所有物理參數必須定義為 `@export var`，方便企劃調整。
- 嚴格檢查 `collision_layer` 與 `collision_mask`。
