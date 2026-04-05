---
id: ISSUE-010
title: "[Producer] level 與關卡 schema（含勝負條件）"
status: todo
source: design/game/mvp.md 第 8 節（P0 level）
primary_skill: game_designer
tags: [producer, level, schema, mvp1]
---

# [Producer] level 與關卡 schema（含勝負條件）

## Description

補齊 `design/game/system/level.md`，並提供 **關卡 schema 說明**（可同檔或獨立 `level_schema.md`）：欄位定義、小／中／大類型意義、MVP1 最小欄位集、**勝利／失敗條件類型與參數**（與 Producer 既定「由 schema 表達」一致）。

## Required Skills

- `game_designer`（主）
- `systems_architect`（選）：若需預想 Godot 載入欄位命名

## Acceptance Criteria

- [ ] **勝負條件** 能以資料表達；類型與參數 **列舉清楚**，MVP1 可先只支援子集並標 Phase 2。
- [ ] 小／中／大類型 **定義可執行**（影響版面、回合、或僅標籤需明說）。
- [ ] 與 **ISSUE-013** 成果 **對齊或明確分工**（誰是 canonical schema：以 Producer 本文件為語意來源，013 可將其收斂為 ERD／儲存格式）。

## Dependencies

- **強建議與 ISSUE-013 並行或先出草稿再由 013 形式化**。
