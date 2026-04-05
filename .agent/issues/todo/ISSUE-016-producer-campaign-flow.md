---
id: ISSUE-016
title: "[Producer] 戰役流程與結束條件"
status: todo
source: design/game/mvp.md 第 8 節（P1 戰役）
primary_skill: game_designer
tags: [producer, campaign, mvp1]
---

# [Producer] 戰役流程與結束條件

## Agent 協作模式（硬性）

- **擁有者**：本 ISSUE 對應之 `design/game/` 檔案，**規則與敘述由 Producer 定稿**。
- **Agent 應做**：以 **問答、核對、缺口盤點** 為主——對照 `design/game/mvp.md` 與下方 Acceptance Criteria，指出 **不足以實作**、**歧義**、與 glossary／他檔 **潛在衝突**；輸出 **待 Producer 回答的具體問題**；可建議 **小節標題或檢核表**，但 **不代替 Producer 寫滿規格內文**。
- **禁止**：未經 Producer **明示委託**（例如「幫我起草我再改」），即 **代寫或覆寫整份企劃**、或將自行推論當成定案寫入 `design/`。
- **實作標準**：定稿後應達到 **Developer 無需臆測玩法**；不足處應標 `[待 Producer 定]` 或留在對話追問，**不可腦補定案**。
- **例外**：Producer 明確要求草稿時，產出須標 **草稿／待 Producer 審**。

## Description

撰寫或併入 `design/game/基礎設定.md`：從進入戰役 → 戰鬥 → 結算（含遺物過渡）→ 下一關的 **流程**；MVP1 為 **無限推進** 或 **有限章節** 須 **明定**。

## Required Skills

- `game_designer`（主）

## Acceptance Criteria

- [ ] 流程 **有步驟列點**，且與 `combat.md`、`mvp.md` 第 5 節 **無矛盾**。
- [ ] **結束條件**（若無限推進亦需說明「無結局迴圈」之玩家體驗邊界）。
- [ ] 若獨立成章，更新 `context_index.md`。

## Dependencies

- 與 **ISSUE-009**、**ISSUE-012**、**ISSUE-015** **一併驗收**較佳。
