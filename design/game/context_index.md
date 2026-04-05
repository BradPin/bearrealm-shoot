# Design Context Index（設計文件索引）

> **目的**：提供 Agent / 企劃撰寫者一個「閱讀順序 + 關聯文件清單」的單一入口。  
> 任何新增/改名/搬移的 `design/game/` 設計文件，請**優先更新本檔**，避免需要同步修改 `.agent/skills/*/SKILL.md`。

---

## 必讀（Glossary-first）

1. `design/game/glossary.md`  
   - 統一術語對照表。**閱讀任何 `design/game/` 文件前，先讀它。**
2. `design/game/mvp.md`  
   - **MVP1 範圍**（遊玩模式、In/Out、遺物過渡策略、驗收與 Producer 文件清單）。實作或收斂需求時優先對齊。
3. `design/game/design_markdown_conventions.md`（**選讀**）  
   - **純 Markdown 企劃** 的目錄／命名、`context_index` 更新時機、`system/*.md` 慣例、與 **ISSUE-013／014** 分工、可複製檢查清單。  
   - **撰寫或搬移** `design/game/**/*.md` 時建議先讀。

---

## 世界觀 / 核心前提

- `design/game/世界觀.md`
- `design/game/基礎設定.md`

---

## 系統設計（依需求選讀）

- `design/game/system/combat.md`
- `design/game/system/level.md`
- `design/game/system/marble.md`
- `design/game/system/relic-weave.md`

---

## 資料表 / 視覺基調

- `design/game/陣營資訊.csv`
- `design/vibe.md`

---

## 模板（企劃維護）

- `design/game/templates/system_spec_checklist.md` — 新開或大修 `system/*.md` 時可複製的檢查清單（詳見 `design_markdown_conventions.md`）。

