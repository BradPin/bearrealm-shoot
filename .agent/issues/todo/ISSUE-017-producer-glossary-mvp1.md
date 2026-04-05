---
id: ISSUE-017
title: "[Producer] Glossary：MVP1 用語與維護規則"
status: todo
source: design/game/mvp.md 第 8 節（P0 glossary）
primary_skill: game_designer
tags: [producer, glossary, mvp1]
---

# [Producer] Glossary：MVP1 用語與維護規則

## Agent 協作模式（硬性）

- **擁有者**：本 ISSUE 對應之 `design/game/` 檔案，**規則與敘述由 Producer 定稿**。
- **Agent 應做**：以 **問答、核對、缺口盤點** 為主——對照 `design/game/mvp.md` 與下方 Acceptance Criteria，指出 **不足以實作**、**歧義**、與 glossary／他檔 **潛在衝突**；輸出 **待 Producer 回答的具體問題**；可建議 **小節標題或檢核表**，但 **不代替 Producer 寫滿規格內文**。
- **禁止**：未經 Producer **明示委託**（例如「幫我起草我再改」），即 **代寫或覆寫整份企劃**、或將自行推論當成定案寫入 `design/`。
- **實作標準**：定稿後應達到 **Developer 無需臆測玩法**；不足處應標 `[待 Producer 定]` 或留在對話追問，**不可腦補定案**。
- **例外**：Producer 明確要求草稿時，產出須標 **草稿／待 Producer 審**。

## Description

`design/game/glossary.md` 為全專案術語 SSOT。本卡負責兩段（**不必在寫其他企劃前整張做完**）：

1. **早階（可併入 ISSUE-007）**：**維護規則**——新名詞先入表、與 `context_index`／系統文件如何互相引用；寫企劃時可暫用「待入 glossary」註記。
2. **晚階（建議在 ISSUE-009～016 主要稿完成後）**：依 MVP1 範圍 **掃描並補齊** 關卡／遺物／戰役等文件已出現的專有名詞（或明確標「同義禁用」）。

> **編號**：本卡為 **017**，排在 **015、016** 之後；再進行 **018**。

## Required Skills

- `game_designer`（主）

## Acceptance Criteria

- [ ] 書面 **glossary 維護規則**（簡短即可，避免與 **ISSUE-007** 重複時互相引用）。
- [ ] MVP1 相關新詞已 **入表或刻意排除並註明理由**。
- [ ] 與 `combat`／`level`／`relic-weave` 等文件用語 **無矛盾**（若他卡先完成，需做一次對照）。

## Dependencies

- **晚階掃尾** 建議在 **ISSUE-009～016** 之後執行，才會知道完整專有名詞集合。
- 早階「維護規則」可與 **ISSUE-007** 一併完成。
