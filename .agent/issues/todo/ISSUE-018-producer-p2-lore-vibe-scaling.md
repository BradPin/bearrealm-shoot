---
id: ISSUE-018
title: "[Producer] P2：數值縮放、世界觀一致性、vibe"
status: todo
source: design/game/mvp.md 第 8 節（P2）
primary_skill: game_designer
tags: [producer, p2, lore, vibe, balancing]
---

# [Producer] P2：數值縮放、世界觀一致性、vibe

## Agent 協作模式（硬性）

- **擁有者**：本 ISSUE 對應之 `design/game/` 檔案，**規則與敘述由 Producer 定稿**。
- **Agent 應做**：以 **問答、核對、缺口盤點** 為主——對照 `design/game/mvp.md` 與下方 Acceptance Criteria，指出 **不足以實作**、**歧義**、與 glossary／他檔 **潛在衝突**；輸出 **待 Producer 回答的具體問題**；可建議 **小節標題或檢核表**，但 **不代替 Producer 寫滿規格內文**。
- **禁止**：未經 Producer **明示委託**（例如「幫我起草我再改」），即 **代寫或覆寫整份企劃**、或將自行推論當成定案寫入 `design/`。
- **實作標準**：定稿後應達到 **Developer 無需臆測玩法**；不足處應標 `[待 Producer 定]` 或留在對話追問，**不可腦補定案**。
- **例外**：Producer 明確要求草稿時，產出須標 **草稿／待 Producer 審**。

## Description

MVP1 可淺做，但須避免與戰鬥規則矛盾，並讓美術有依據。本卡合併 `mvp.md` P2 三項：

1. **關卡數值縮放**（新建建議 `system/progression_scaling.md`）：公式或簡表；MVP1 若用常數需註明。
2. **`世界觀.md`／`基礎設定.md`**：與已定戰鬥／戰役規則 **盤點無矛盾**（不要求長篇擴寫）。
3. **`design/vibe.md`**：必要時補充，供 Agent 產出資產對齊。

## Required Skills

- `game_designer`（主）
- `art_director`（選）：僅 vibe 視覺段落若需共筆

## Acceptance Criteria

- [ ] 縮放策略 **有書面結論**（即使暫為「MVP1 固定表」）。
- [ ] 世界觀與基礎設定 **與 P0 戰鬥企劃無衝突**（衝突清單為空或已解決）。
- [ ] `vibe.md` 足以支撐 MVP1 美術範圍或明列「沿用預設」。

## Dependencies

- **建議在 ISSUE-009～017 主要完成後** 做一次總盤點。
