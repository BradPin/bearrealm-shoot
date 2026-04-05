---
id: ISSUE-013
title: "[Planning] Schema／ERD 設計與儲存載體評選"
status: todo
source: design/game/mvp.md（level schema、遺物資料形狀）+ User plan-card 需求
primary_skill: game_designer
tags: [planning, schema, erd, data-model]
---

# [Planning] Schema／ERD 設計與儲存載體評選

## Description

將遊戲 **可資料化** 的內容（關卡、勝負條件、遺物鏈、彈珠屬性、敵方行為模板等）收斂為 **Schema／ERD 層級** 的規格，並 **評選 MVP1 與後續擴充適用的儲存與編修載體**。

須涵蓋（可拆成子文件，但需單一索引入口）：

1. **實體與關係（ERD 或等價說明）**  
   - 關卡、戰鬥單位、遺物、掉落／解鎖規則等之間的關聯（與 `glossary` 用語一致）。
2. **欄位級 schema**  
   - 與 `mvp.md` 對齊：**勝利／失敗條件** 必須可由關卡資料表達；預留擴充欄位策略。
3. **儲存載體決策（待選：CSV／SQLite／JSON 或其他）**  
   - 從 **Producer 編修體驗、版本控管 diff、Godot 載入成本、驗證工具** 等面向做簡短比較，產出 **建議方案與 MVP1 預設**（可為 ADR 式一頁）。  
   - 若 MVP1 暫用過渡格式，需寫明 **遷移到目標格式的條件或時機**。
4. **與程式邊界**  
   - 哪些欄位由企劃資料驅動、哪些仍屬程式常數（避免任務發散）。

## Required Skills

- `game_designer`（主）：實體、規則與欄位語意。
- `systems_architect`（選）：Godot 資源／載入與專案慣例銜接。
- `developer`（選）：若需雛形載入或驗證腳本設計。

## Acceptance Criteria

- [ ] 有一份 **ERD 或等價圖／表**（可為 Mermaid、圖片、或結構化 md），涵蓋 MVP1 必備實體。
- [ ] **關卡 schema** 至少包含：**勝利條件類型與參數** 的欄位定義（與 `system/level.md` 對齊或明確標註取代關係）。
- [ ] 完成 **儲存載體評選結論**（建議格式 + 理由 + MVP1 是否採用過渡方案）。
- [ ] `design/game/context_index.md` 或專用索引 **加入 schema 規格入口**。
- [ ] 與 **ISSUE-014** 交接清楚：**資料文件** 如何符合本 schema（檔名、必填欄位、範例）。

## Notes

- 本卡以 **企劃／資料規格** 為主；大量實作載入器可另開工程 ISSUE，但本卡應給出足夠明確的 **目標格式與範例片段**。
