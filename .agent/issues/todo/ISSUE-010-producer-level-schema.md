---
id: ISSUE-010
title: "[Producer] level 與關卡 schema（含勝負條件）"
status: todo
source: design/game/mvp.md 第 8 節（P0 level）
primary_skill: game_designer
tags: [producer, level, schema, mvp1]
---

# [Producer] level 與關卡 schema（含勝負條件）

## Agent 協作模式（硬性）

- **擁有者**：本 ISSUE 對應之 `design/game/` 檔案，**規則與敘述由 Producer 定稿**。
- **Agent 應做**：以 **問答、核對、缺口盤點** 為主——對照 `design/game/mvp.md` 與下方 Acceptance Criteria，指出 **不足以實作**、**歧義**、與 glossary／他檔 **潛在衝突**；輸出 **待 Producer 回答的具體問題**；可建議 **小節標題或檢核表**，但 **不代替 Producer 寫滿規格內文**。
- **禁止**：未經 Producer **明示委託**（例如「幫我起草我再改」），即 **代寫或覆寫整份企劃**、或將自行推論當成定案寫入 `design/`。
- **實作標準**：定稿後應達到 **Developer 無需臆測玩法**；不足處應標 `[待 Producer 定]` 或留在對話追問，**不可腦補定案**。
- **例外**：Producer 明確要求草稿時，產出須標 **草稿／待 Producer 審**。

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
