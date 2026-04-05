---
id: ISSUE-014
title: "[Planning] 資料內容製作（關卡等）與驗證流程"
status: todo
source: design/game/mvp.md（內容清單、小中大關卡）+ User plan-card 需求
primary_skill: game_designer
tags: [planning, data-authoring, levels, validation]
---

# [Planning] 資料內容製作（關卡等）與驗證流程

## Description

在 **ISSUE-013** 的 **schema／載體** 定案（或過渡方案）之後，建立 **實際資料內容** 的製作與維護方式：例如「設計了三個關卡」時，**詳細內容存放位置、命名、版本與驗證**。

須涵蓋：

1. **內容庫結構**  
   - 建議目錄（例如 `design/game/data/` 或 `assets/...` 僅放匯出物—由決策明定）；關卡／敵方模板／遺物列舉等 **一覽與單筆檔案** 的組織方式。
2. **與 `mvp.md` 對齊**  
   - MVP1 **內容清單**（關卡 ID、模板數量）如何對應到實際檔案；小／中／大類型標記方式。
3. **驗證**  
   - **最小驗證規則**（必填欄位、勝利條件類型合法、引用 ID 存在）；若可自動化，描述工具或指令（不必在本卡內實作完整 CI，但需定義「何謂通過」）。
4. **範例集**  
   - 至少 **1～3 筆** 完整範例（可為真實 MVP1 關卡或沙盒），作為 Producer 與 Agent 的共同參考。

## Required Skills

- `game_designer`（主）：內容欄位填寫與試玩意義。
- `context_reviewer`（選）：目錄與索引是否利於協作。
- `developer`（選）：驗證腳本雛形若需要。

## Acceptance Criteria

- [ ] 文件化 **內容檔案放置規範**（路徑、命名、與 schema 的對應關係）。
- [ ] **MVP1 最小內容集** 有明確列表（可連結到實際檔或 issue 子清單），且與 `mvp.md` 第 8 節「內容清單」一致或明確更新 `mvp.md`。
- [ ] **驗收規則** 書面化（人工檢查表或自動檢查項）。
- [ ] 至少一份 **端到端範例**（從關卡資料 → 可被理解的戰鬥設定／勝利條件），格式符合 **ISSUE-013** 結論。
- [ ] `context_index.md`（或 data 專用索引）**指向內容製作說明**。

## Dependencies

- **建議在 ISSUE-013 完成或至少有過渡 schema 後執行**；若並行，需在卡內註明同步調整機制。

## Notes

- 本卡聚焦 **「資料文件」產製**；純敘述規則仍歸 **ISSUE-007**，schema 定義歸 **ISSUE-013**。
