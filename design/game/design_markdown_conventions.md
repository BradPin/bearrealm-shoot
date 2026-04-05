# 企劃說明文件（純 Markdown）架構與維護

> **用途**：約定 `design/game/` 內 **純文字企劃** 的目錄、命名、章節習慣，以及與 **schema／實際資料**（由其他 Issue 負責）的交叉引用方式。  
> **不決定** CSV／SQLite／JSON 等儲存載體；正式欄位與型別以 **ISSUE-013** 產出為準，內容檔與驗證以 **ISSUE-014** 為準。

---

## 1. 與 `context_index.md` 的關係

| 角色 | 說明 |
| :--- | :--- |
| `design/game/context_index.md` | **單一入口**：閱讀順序、必讀／選讀、相關檔案清單。Agent 與撰寫者優先由此進入，避免散落修改多份 `SKILL.md`。 |
| 本檔 | **維護規約**：何時改名搬檔、如何寫 `system/*.md`、檢查清單、與 `mvp.md` 第 8 節的對照。 |

**閱讀順序（建議）**

1. `glossary.md`（必讀；任何 `design/game/` 文件前）  
2. `mvp.md`（必讀；範圍與 Producer 文件清單）  
3. 本檔（**撰寫／維護企劃 MD 時**選讀；onboarding 想一次搞懂目錄時選讀）  
4. `context_index.md` 其餘連結（依任務選讀）

---

## 2. 目錄與命名慣例（純 Markdown）

| 區域 | 路徑慣例 | 內容 |
| :--- | :--- | :--- |
| 術語 | `design/game/glossary.md` | 統一術語表；新名詞先進表再引用。 |
| 範圍與清單 | `design/game/mvp.md` | MVP1 In/Out、驗收、Producer 文件清單（第 8 節）。 |
| 系統企劃 | `design/game/system/<topic>.md` | 單一系統一份主檔；檔名小寫、`kebab-case` 英文（如 `combat.md`、`relic-weave.md`）。 |
| 世界觀／設定 | `design/game/*.md` | 如 `世界觀.md`、`基礎設定.md`；與戰鬥規則不得矛盾。 |
| 結構化表 | `design/game/*.csv` | 如 `陣營資訊.csv`；**非** schema 定義，僅企劃用表。 |
| 規格書（功能向） | `design/game/specs/SPEC-<title>.md` | 依 `.agent/skills/game_designer/SKILL.md`；與 `system/` 分檔，避免混用命名。 |
| 實體表 | `design/game/entities/` | 角色／敵人／道具等實體說明。 |
| 模板／檢查表 | `design/game/templates/` | 可複製範本（本專案已提供 `templates/system_spec_checklist.md`）。 |

**檔名變更或新增時**：同步更新 `context_index.md` 與本檔第 5 節對照表（若該項被列於 `mvp.md` 第 8 節）。

---

## 3. 何時必須更新 `context_index.md`

在下列情況 **應立即更新** `design/game/context_index.md`：

- 新增、刪除、更名或搬移任何會被 Agent／企劃引用的 `design/game/**/*.md`（含 `system/`、`specs/`）。  
- 調整「必讀／選讀」策略或閱讀順序。  
- 新增與主流程對齊的 **跨檔索引**（例如新系統主檔）。

下列情況 **可不改 index**（但建議在該檔開頭或 PR 說明註記）：

- 僅修正錯字、用語對齊 `glossary`、不改路徑。  
- 僅在單一檔內增刪章節、未新增對外連結需求。

---

## 4. `system/*.md` 撰寫慣例

### 4.1 建議章節結構

1. **標題與一句話目的**  
2. **與其他文件的邊界**（見下節「交叉引用」）  
3. **MVP1 與長期**（可用小節「MVP1」與「長期／Phase 2」分開；MVP1 簡化處須標 *僅 MVP1*）  
4. **規則敘述**（表格、列表、流程）  
5. **待決／待 schema**（避免在 MD 內寫死將由 ISSUE-013 定義的欄位型別）

### 4.2 術語

- 正文使用之遊戲術語須與 `glossary.md` 一致；若需新術語，先擴充 glossary 並經 Producer 確認。

### 4.3 與 schema／資料文件的分工（不重複定義）

| 層級 | 歸屬 | 純 MD 企劃應寫什麼 |
| :--- | :--- | :--- |
| 玩法語意、流程、邊界案例 | `system/*.md` 等 | 人讀的規則與順序（例：何時檢查勝負、同時彈射語意）。 |
| 欄位名稱、型別、列舉值、預設、驗證規則 | **ISSUE-013** 產出之 schema／ADR | MD 僅 **連結與摘要**，不重複貼「正式定義」。 |
| 實際關卡／模板／ID 清單與範例檔 | **ISSUE-014**（及後續內容庫目錄） | MD 可列 **需求與索引句**（例：「勝利條件類型見 level schema」）。 |

**交叉引用句式範例**

- 「關卡行為與勝利條件之 **欄位定義** 見 **ISSUE-013** 之 level schema；本檔僅描述 **語意與流程**。」  
- 「具體關卡 JSON／表格式內容與驗證流程見 **ISSUE-014**。」

---

## 5. `mvp.md` 第 8 節：文字企劃項與實際路徑對照

| 優先序 | `mvp.md` 建議項 | 實際或建議路徑 | 狀態 |
| :--- | :--- | :--- | :--- |
| P0 | `glossary.md` | `design/game/glossary.md` | 已有 |
| P0 | `system/combat.md` | `design/game/system/combat.md` | 已有 |
| P0 | `system/level.md` + 關卡 schema 說明 | `design/game/system/level.md`；欄位級 schema 見 **ISSUE-010**、**ISSUE-013** | 敘述已有；schema 待 013／010 |
| P0 | `system/marble.md` | `design/game/system/marble.md` | 已有 |
| P0 | 單人／多人與 AI 代管（建議 `session_multiplayer.md`） | `design/game/system/session_multiplayer.md`（建議路徑） | **待建** |
| P1 | `relic-weave.md` + MVP1 附錄 | `design/game/system/relic-weave.md`；MVP1 細節收斂見 **ISSUE-012** | 檔案已有；MVP1 附錄待補 |
| P1 | MVP1 內容清單（建議 `mvp1_content_backlog.md`） | `design/game/mvp1_content_backlog.md`（建議路徑） | **待建**（對齊 **ISSUE-015**） |
| P1 | 戰役流程與結束條件 | 建議併入 `design/game/基礎設定.md` 或獨立短篇；見 **ISSUE-016** | **待整合** |
| P2 | 關卡數值縮放（建議 `progression_scaling.md`） | `design/game/system/progression_scaling.md`（建議路徑） | **待建** |
| P2 | `世界觀.md` / `基礎設定.md` | `design/game/世界觀.md`、`design/game/基礎設定.md` | 已有 |
| P2 | `vibe.md` | `design/vibe.md` | 已有（根目錄在 `design/`，非 `game/`） |

---

## 6. 與 ISSUE-013、ISSUE-014 的分工（避免同一規則兩處定義）

| Issue | 標題（摘要） | 負責內容 | 純 Markdown 企劃不做的事 |
| :--- | :--- | :--- | :--- |
| **ISSUE-013** | Schema／ERD 與儲存載體評選 | 實體關係、欄位級 schema、格式選型與 ADR、與程式載入邊界 | 不在 `system/*.md` 內寫「最終欄位型別與儲存格式」長表取代之 |
| **ISSUE-014** | 資料內容製作與驗證流程 | 內容庫目錄、命名、範例資料、最小驗證規則 | 不在企劃 MD 內維護大量實例資料（僅索引與需求） |
| **本檔（ISSUE-007）** | 企劃 MD 架構 | 目錄命名、`context_index` 規則、模板、對照表、交叉引用句式 | 不選 CSV／SQLite／JSON；不寫完整 schema |

**協作順序**：語意與流程（MD）→ schema 定案（013）→ 內容與驗證（014）。MD 在 013 定案後應 **回頭加連結**，刪除或改寫任何與 schema 衝突的暫定欄位描述。

---

## 7. 可複製：新開 `system/<topic>.md` 檢查清單

（完整可另存版本見 `design/game/templates/system_spec_checklist.md`。）

```markdown
## 新系統企劃檔檢查（貼入 `system/<topic>.md` 草稿末尾，完成後刪除）

- [ ] 已讀 `glossary.md`，正文用語與表內一致
- [ ] 已說明與 `mvp.md` MVP1 範圍的對齊或標註「僅長期」
- [ ] 已標註與其他 `system/*.md` 的邊界（不重複貼他檔規則）
- [ ] 勝利條件、欄位、ID 等 **正式定義** 僅指向 ISSUE-013／既有 schema 文件，未在本文重複定義
- [ ] MVP1 簡化處皆有「僅 MVP1」或 Phase 標記
- [ ] 已更新 `design/game/context_index.md`（若為新檔或路徑變更）
- [ ] 若新增術語，已排入 `glossary.md` 更新（或註明待 Producer 批准）
```

---

## 8. 修訂紀錄

| 日期 | 說明 |
| :--- | :--- |
| 2026-04-05 | 初版：目錄命名、`context_index` 更新規則、system 慣例、mvp 第 8 節對照、013／014 分工、檢查清單。 |
