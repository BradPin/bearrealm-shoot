---
id: ISSUE-018
title: "[Producer] P2：數值縮放、世界觀一致性、vibe"
status: todo
source: design/game/mvp.md 第 8 節（P2）
primary_skill: game_designer
tags: [producer, p2, lore, vibe, balancing]
---

# [Producer] P2：數值縮放、世界觀一致性、vibe

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
