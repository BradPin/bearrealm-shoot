---
id: ISSUE-003
title: "[Core] Slingshot Physics & CharacterBody2D"
status: TODO
tags: [physics, gdscript, core]
primary_skill: developer
---
# [Core] Slingshot Physics & CharacterBody2D

## Description
實作類怪物彈珠的核心彈射機制。使用 `CharacterBody2D` 取代內建物理引擎以獲得更高精確度的控制，並實作向量反彈邏輯。

## Context
目標是達成精確的彈射手感，包含：
1. 觸碰並拉動時的預測線。
2. 碰撞牆壁或敵人時的向量反彈 (`velocity.bounce(normal)`)。
3. 碰撞後的動能衰減係數 (Bounciness) 調整。

## Tasks
1. [ ] 建立 `PlayerMarble.tscn` (CharacterBody2D)。
2. [ ] 實作 `_input` 處理拉動與放開的向量計算。
3. [ ] 實作彈射邏輯與碰撞反彈代碼。
4. [ ] 建立基礎測試場景 `Main.tscn` 並加上牆壁邊界。

## Acceptance Criteria
- [ ] 彈珠能透過滑鼠/觸碰拉動並朝反方向彈射。
- [ ] 碰撞牆壁時能以正確角度反彈，不發生穿牆。
- [ ] 提供參數可調整彈射力道上限。
