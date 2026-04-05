---
id: ISSUE-009
title: "[Producer] combat.md：MVP1 可實作戰鬥規格"
status: todo
source: design/game/mvp.md 第 8 節（P0 combat）
primary_skill: game_designer
tags: [producer, combat, mvp1]
---

# [Producer] combat.md：MVP1 可實作戰鬥規格

## Agent 協作模式（硬性）

- **擁有者**：本 ISSUE 對應之 `design/game/` 檔案，**規則與敘述由 Producer 定稿**。
- **Agent 應做**：以 **問答、核對、缺口盤點** 為主——對照 `design/game/mvp.md` 與下方 Acceptance Criteria，指出 **不足以實作**、**歧義**、與 glossary／他檔 **潛在衝突**；輸出 **待 Producer 回答的具體問題**；可建議 **小節標題或檢核表**，但 **不代替 Producer 寫滿規格內文**。
- **禁止**：未經 Producer **明示委託**（例如「幫我起草我再改」），即 **代寫或覆寫整份企劃**、或將自行推論當成定案寫入 `design/`。
- **實作標準**：定稿後應達到 **Developer 無需臆測玩法**；不足處應標 `[待 Producer 定]` 或留在對話追問，**不可腦補定案**。
- **例外**：Producer 明確要求草稿時，產出須標 **草稿／待 Producer 審**。

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
