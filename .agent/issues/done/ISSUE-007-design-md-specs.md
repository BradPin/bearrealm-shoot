---
id: ISSUE-007
title: "[Planning] 企劃說明文件（純 Markdown）架構與維護"
status: done
source: design/game/mvp.md 第 8 節（Producer 文件清單）+ User plan-card 需求
primary_skill: game_designer
tags: [planning, design-docs, markdown]
---

# [Planning] 企劃說明文件（純 Markdown）架構與維護

## Description

建立並維護 **純 Markdown 說明向** 企劃文件的結構，使 Producer 的玩法／流程敘述與 Agent 實作有穩定對照，且新對話能以低 token 對齊。

範圍包含（可視需要微調檔名，但需更新索引）：

- 與 `design/game/context_index.md` 的 **閱讀順序、必讀／選讀** 關係。
- 系統說明檔慣例（例如 `system/*.md`）：章節結構、術語必引用 `glossary.md`、MVP1 與長期規格分節方式。
- `mvp.md` 所列 P0/P1 **文字企劃**（`combat`、`marble`、`session_multiplayer` 概念、戰役流程等）的 **模板或撰寫檢查清單**（可為單一 `design/game/templates/` 或併入各檔開頭說明）。
- 與 **schema／資料文件** 的交叉引用約定（例如「關卡行為見 level schema；敘述見 combat」），避免重複定義衝突。

## Required Skills

- `game_designer`（主）：規格結構、檢查清單。
- `context_reviewer`（選）：索引與 token 路徑是否利於 onboarding。

## Acceptance Criteria

- [x] 文件中有明確的 **目錄／命名慣例**（純 MD 類）與 **何時更新 `context_index.md`** 的規則。
- [x] 至少一份 **可複製的模板或檢查清單**（適用於系統說明或新開 `system/*.md`）。
- [x] `mvp.md` P0 文字企劃項與實際檔案路徑 **對照表或註記**（缺檔則標「待建」），避免 Agent 猜路徑。
- [x] 說明如何與 **ISSUE-013**（schema）／**ISSUE-014**（資料內容）**分工**，不重複定義同一規則。

## Notes

- 本卡 **不** 決定 CSV／SQLite／JSON；僅約定 Markdown 層如何指向「正式資料定義」。
- **ISSUE-003～005**（核心工程）可與企劃向 ISSUE **並行**。
- **ISSUE-008 起**（企劃／Producer 與 013／014 規劃向）：各卡頂部 **「Agent 協作模式（硬性）」** 為 Agent 行為準則；並與 `.agent/skills/game_designer/SKILL.md` 之 **Producer 主筆模式** 一致（問答與缺口盤點為主，禁止未委託即代寫定稿）。
