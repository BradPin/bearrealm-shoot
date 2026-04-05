---
id: ISSUE-011
title: "[Producer] marble.md：彈珠屬性與 MVP1 取捨"
status: todo
source: design/game/mvp.md 第 8 節（P0 marble）
primary_skill: game_designer
tags: [producer, marble, mvp1]
---

# [Producer] marble.md：彈珠屬性與 MVP1 取捨

## Agent 協作模式（硬性）

- **擁有者**：本 ISSUE 對應之 `design/game/` 檔案，**規則與敘述由 Producer 定稿**。
- **Agent 應做**：以 **問答、核對、缺口盤點** 為主——對照 `design/game/mvp.md` 與下方 Acceptance Criteria，指出 **不足以實作**、**歧義**、與 glossary／他檔 **潛在衝突**；輸出 **待 Producer 回答的具體問題**；可建議 **小節標題或檢核表**，但 **不代替 Producer 寫滿規格內文**。
- **禁止**：未經 Producer **明示委託**（例如「幫我起草我再改」），即 **代寫或覆寫整份企劃**、或將自行推論當成定案寫入 `design/`。
- **實作標準**：定稿後應達到 **Developer 無需臆測玩法**；不足處應標 `[待 Producer 定]` 或留在對話追問，**不可腦補定案**。
- **例外**：Producer 明確要求草稿時，產出須標 **草稿／待 Producer 審**。

## Description

補齊 `design/game/system/marble.md`：單一彈珠屬性、魔力取得方式在 MVP1 的取捨、若 AI 代管影響規則則一併說明。

## Required Skills

- `game_designer`（主）

## Acceptance Criteria

- [ ] MVP1 **最小屬性集** 與 **刻意延後項目** 有明確列表。
- [ ] 與 `combat.md`（技能／魔力）、`session_multiplayer`（誰操作哪顆球）**一致**。
- [ ] 與 `glossary.md` 一致。

## Dependencies

- 建議在 **ISSUE-008** 草稿後 **對照 AI 代管段落**。
