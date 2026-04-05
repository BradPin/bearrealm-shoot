---
id: ISSUE-012
title: "[Producer] relic-weave：長期規格 + MVP1 附錄（D／固定鏈）"
status: todo
source: design/game/mvp.md 第 8 節（P1 relic）+ mvp.md 第 4 節
primary_skill: game_designer
tags: [producer, relic, mvp1]
---

# [Producer] relic-weave：長期規格 + MVP1 附錄（D／固定鏈）

## Agent 協作模式（硬性）

- **擁有者**：本 ISSUE 對應之 `design/game/` 檔案，**規則與敘述由 Producer 定稿**。
- **Agent 應做**：以 **問答、核對、缺口盤點** 為主——對照 `design/game/mvp.md` 與下方 Acceptance Criteria，指出 **不足以實作**、**歧義**、與 glossary／他檔 **潛在衝突**；輸出 **待 Producer 回答的具體問題**；可建議 **小節標題或檢核表**，但 **不代替 Producer 寫滿規格內文**。
- **禁止**：未經 Producer **明示委託**（例如「幫我起草我再改」），即 **代寫或覆寫整份企劃**、或將自行推論當成定案寫入 `design/`。
- **實作標準**：定稿後應達到 **Developer 無需臆測玩法**；不足處應標 `[待 Producer 定]` 或留在對話追問，**不可腦補定案**。
- **例外**：Producer 明確要求草稿時，產出須標 **草稿／待 Producer 審**。

## Description

更新 `design/game/system/relic-weave.md`：維持與長期設計及 `glossary.md`（能量、Inactive、孔位等）一致。

另增 **MVP1 小節**：明確採 **方案 D**（極簡 UI + 真資料）或備援 **固定鏈 + 每關隨機開放** 的規則；凡 MVP1 簡化須標 **「僅 MVP1」**。

## Required Skills

- `game_designer`（主）

## Acceptance Criteria

- [ ] MVP1 流程 **可被程式與企劃同時遵循**（含掉落／開節點若用備援的具體規則）。
- [ ] 與 **ISSUE-013** 中遺物實體 **可對齊**（欄位語意不打架）。
- [ ] `glossary` 用語一致。

## Dependencies

- 建議與 **ISSUE-013**、**ISSUE-015** **對齊**。
