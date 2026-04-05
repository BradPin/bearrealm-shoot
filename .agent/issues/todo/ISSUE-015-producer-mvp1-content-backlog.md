---
id: ISSUE-015
title: "[Producer] MVP1 內容清單（關卡／敵人／遺物 ID）"
status: todo
source: design/game/mvp.md 第 8 節（P1 content backlog）
primary_skill: game_designer
tags: [producer, content, mvp1]
---

# [Producer] MVP1 內容清單（關卡／敵人／遺物 ID）

## Agent 協作模式（硬性）

- **擁有者**：本 ISSUE 對應之 `design/game/` 檔案，**規則與敘述由 Producer 定稿**。
- **Agent 應做**：以 **問答、核對、缺口盤點** 為主——對照 `design/game/mvp.md` 與下方 Acceptance Criteria，指出 **不足以實作**、**歧義**、與 glossary／他檔 **潛在衝突**；輸出 **待 Producer 回答的具體問題**；可建議 **小節標題或檢核表**，但 **不代替 Producer 寫滿規格內文**。
- **禁止**：未經 Producer **明示委託**（例如「幫我起草我再改」），即 **代寫或覆寫整份企劃**、或將自行推論當成定案寫入 `design/`。
- **實作標準**：定稿後應達到 **Developer 無需臆測玩法**；不足處應標 `[待 Producer 定]` 或留在對話追問，**不可腦補定案**。
- **例外**：Producer 明確要求草稿時，產出須標 **草稿／待 Producer 審**。

## Description

建立 `design/game/mvp1_content_backlog.md`（或等價檔名），列出 MVP1 **最小可跑通** 的內容 ID：關卡、敵人／技能模板、遺物等；數量可少，但須能支撐戰役循環。

## Required Skills

- `game_designer`（主）

## Acceptance Criteria

- [ ] 清單與 `mvp.md`（小中大、數量預期）**一致或明確修訂 mvp.md**。
- [ ] 每個 ID **有類型與用途一句話**，便於 **ISSUE-014** 對檔。
- [ ] 已列入 `context_index.md`（若採獨立檔）。

## Dependencies

- 建議在 **ISSUE-010**、**ISSUE-012** **有初稿後** 定稿，避免 ID 漂移。
