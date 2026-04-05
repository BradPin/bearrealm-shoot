---
id: ISSUE-008
title: "[Producer] session_multiplayer：單機 1+3 與日後多人邊界"
status: todo
source: design/game/mvp.md 第 8 節（P0 session）
primary_skill: game_designer
tags: [producer, multiplayer, session, mvp1]
---

# [Producer] session_multiplayer：單機 1+3 與日後多人邊界

## Agent 協作模式（硬性）

- **擁有者**：本 ISSUE 對應之 `design/game/` 檔案，**規則與敘述由 Producer 定稿**。
- **Agent 應做**：以 **問答、核對、缺口盤點** 為主——對照 `design/game/mvp.md` 與下方 Acceptance Criteria，指出 **不足以實作**、**歧義**、與 glossary／他檔 **潛在衝突**；輸出 **待 Producer 回答的具體問題**；可建議 **小節標題或檢核表**，但 **不代替 Producer 寫滿規格內文**。
- **禁止**：未經 Producer **明示委託**（例如「幫我起草我再改」），即 **代寫或覆寫整份企劃**、或將自行推論當成定案寫入 `design/`。
- **實作標準**：定稿後應達到 **Developer 無需臆測玩法**；不足處應標 `[待 Producer 定]` 或留在對話追問，**不可腦補定案**。
- **例外**：Producer 明確要求草稿時，產出須標 **草稿／待 Producer 審**。

## Description

新建 `design/game/system/session_multiplayer.md`（路徑可依慣例調整並更新 `context_index.md`）。

內容須涵蓋：`mvp.md` 已定——MVP1 僅 **1 真人 + 3 AI**；未來多人時 **席位、操作權、AI 補位**；**單機時無需同步** vs **未來需同步的邊界**（概念層即可，不必實作網路）。

## Required Skills

- `game_designer`（主）

## Acceptance Criteria

- [ ] 檔案已建立並列入 `context_index.md`。
- [ ] 1+3 與「空位皆 AI」的 **規則敘述** 與 `mvp.md` 一致。
- [ ] 程式可讀的 **邊界清單**（例如：哪些狀態日後必須單一權威來源），避免實作卡死本機假設時能對照此文。

## Dependencies

- 與 **ISSUE-011**（marble）、**ISSUE-009**（combat）**交叉審閱**。
