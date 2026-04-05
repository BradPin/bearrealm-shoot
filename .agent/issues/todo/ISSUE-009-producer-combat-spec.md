---
id: ISSUE-009
title: "[Producer] combat.md：MVP1 可實作戰鬥規格"
status: todo
source: design/game/mvp.md 第 8 節（P0 combat）
primary_skill: game_designer
tags: [producer, combat, mvp1]
---

# [Producer] combat.md：MVP1 可實作戰鬥規格

## Description

將 `design/game/system/combat.md` 擴寫至 MVP1 所需深度，使程式可依此文實作與測試，無需猜規則。

須涵蓋（依 `mvp.md`）：回合流程、同時彈射、技能自動釋放順序、勝負檢查時機、邊界情況（全靜止、同時觸發等）。

## Required Skills

- `game_designer`（主）

## Acceptance Criteria

- [ ] 上述段落 **可逐條對應狀態機或函式責任**（不要求寫程式，但邏輯閉合）。
- [ ] 與 `glossary.md` 術語一致。
- [ ] 與 `level.md` 中「戰鬥結果判定時機」**無衝突**（若 `level` 先定義勝負欄位，combat 須引用其檢查點）。

## Dependencies

- 建議與 **ISSUE-010**（level）、**ISSUE-017**（glossary 早階規則若已併入 007）**交叉審閱**。
