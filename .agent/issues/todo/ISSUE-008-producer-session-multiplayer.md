---
id: ISSUE-008
title: "[Producer] session_multiplayer：單機 1+3 與日後多人邊界"
status: todo
source: design/game/mvp.md 第 8 節（P0 session）
primary_skill: game_designer
tags: [producer, multiplayer, session, mvp1]
---

# [Producer] session_multiplayer：單機 1+3 與日後多人邊界

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
