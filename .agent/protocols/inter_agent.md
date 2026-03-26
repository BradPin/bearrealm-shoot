# Inter-Agent Protocol (Skills 協作協議)

> Human-in-the-Loop 設計。User 是 Producer，掌控所有階段轉換。
> Agent **在每個 🚧 GATE 必須停下，等 User 的 workflow 指令才推進**。

---

## 1. 核心原則

### 1.1 Producer 控制制
User 是 Producer。Agent 完成一個階段後，報告成果並**等待 User 下達下一個 workflow 指令**。

### 1.2 Workflow 驅動
階段轉換由 User 的 workflow 指令觸發，不由 Agent 自行決定：

| User 指令 | 含義 | 對應 Workflow |
|-----------|------|--------------|
| `/plan <input>` | 開始規劃 | `workflows/plan.md` |
| `/plan-card [source]` | 從文件拆出 ISSUE 卡 | `workflows/plan-card.md` |
| `/feature-start ISSUE-N` | 開始實作某張卡 | `workflows/feature-start.md` |
| `/feature-valid` | 驗證實作成果 | `workflows/feature-valid.md` |
| `/finish` | 收尾當前階段 (auto-detect) | `workflows/finish.md` |
| `review-context` | 審查 Context 健康度 | `workflows/review-context.md` |

### 1.3 Artifact-Driven Handoff
Skills 之間透過**具體檔案**溝通：每個 Skill 產出定義好的檔案，下一個 Skill 消費那些檔案。

---

## 2. 標準協作流

### 🎮 Flow A: 完整規劃 → 實作 (新系統 / 大功能)

```
User 在 design/ 撰寫設計文件
    │
    ▼
User: /plan design/game/system/xxx.md
    │   (或 /plan 我想做一個 xxx 系統)
    │
    ▼  Agent 讀取 → Game Designer 整理 → 產出 PLAN 文件
    │  Output: .agent/plans/PLAN-N-title.md
    │
    ▼  Agent 報告計畫內容
🚧 GATE ── User 審核計畫 ──
    │
    ▼
User: /plan-card
    │   (PM 從 PLAN 拆出 ISSUE 卡)
    │
    ▼  Output: .agent/issues/todo/ISSUE-*.md
    │
    ▼  Agent 列出所有卡片
🚧 GATE ── User 審核卡片、可要求修改 ──
    │
    ▼
User: /finish
    │   (auto-detect: PLAN branch → 提交規劃文件)
    │
    ▼
User: /feature-start ISSUE-7
    │   (挑選一張卡開工)
    │
    ▼  Agent 建分支 → 搬卡 → 調度 Skill → 實作
    │
    ▼  Agent 報告實作成果
🚧 GATE ── User 驗收 ──
    │
    ├─→ User: /feature-valid  (要求 Agent 自檢)
    │
    ▼
User: /finish
    │   (auto-detect: ISSUE branch → 搬卡到 done、commit)
    │
    ▼  回到上面，User 挑下一張: /feature-start ISSUE-8 ...
```

### 🎯 Flow B: 快速拆卡 (設計已完善，跳過 /plan)

```
User: /plan-card design/game/system/戰鬥系統.md
    │   (直接從設計文件拆卡，不經過 /plan)
    │
    ▼  PM 讀取文件 → 產出 ISSUE 卡
    │
🚧 GATE ── User 審核 ──
    │
    ▼
User: /finish → /feature-start ISSUE-N → ...
```

### 🎨 Flow C: 單一資源需求 (不需要拆卡)

```
User: 幫火屬性角色加一張新圖
    │
    ▼  Art Director (讀 Vault → ComfyUI MCP → 處理 → Registry)
    │  Output: assets/<category>/<file>
    │
🚧 GATE ── User 確認滿意 ──
    │
    ▼  Systems Architect 掛載到場景 (如果 User 要求)
```

### 🧹 Flow D: 維護

```
User: review-context
    │
    ▼  Context Reviewer 全自動執行 → 報告
    │
User 確認重大變更
```

---

## 3. Skill 調度規則 (feature-start 內部)

當 `/feature-start` 觸發後，Agent 根據 ISSUE 卡的 **Required Skills** 欄位決定載入哪些 Skill：

| 需求類型 | 載入 Skill | 可能觸發的內部 Workflow |
|---------|-----------|----------------------|
| 角色圖 / UI 圖 / 特效圖 | art_director | create_asset.md |
| 音效 / BGM | audio_designer | create_asset.md |
| 粒子 / Shader | vfx_artist | — |
| 場景節點組裝 | systems_architect | — |
| GDScript 邏輯 | developer | — |
| 動畫 / Tween | animator | — |
| UI 佈局 | ui_designer | — |

**原則**：一張 ISSUE 不一定需要全部 Skill。只載入需要的，節省 token。

---

## 4. Artifact Registry (產出物清單)

| Skill | Output | Location |
|-------|--------|----------|
| Game Designer | Feature Spec / Entity Sheet | `design/game/specs/`, `design/game/entities/` |
| Project Manager | Plan + Issue Cards | `.agent/plans/`, `.agent/issues/` |
| Art Director | Image Assets + Registry | `assets/`, `.agent/asset_registry/art.csv` |
| Audio Designer | Audio Assets + Registry | `assets/audio/`, `.agent/asset_registry/audio.csv` |
| VFX Artist | Particle configs + Shaders | `assets/vfx/`, `.gdshader` files |
| UI Designer | UI Scenes + Themes | `scenes/ui/`, `assets/ui/` |
| Systems Architect | Assembled Scenes | `scenes/` |
| Developer | GDScript Files | co-located with scenes |
| Animator | Animation Resources | Embedded in `.tscn` or `.tres` |

---

## 5. 衝突與阻塞

### 優先順序：
1. **User (Producer)** — 永遠最高。
2. **Game Designer spec** — 定義「做什麼」。
3. **Systems Architect** — 引擎限制下「怎麼做」。
4. **Art/Audio** — 美學限制。
5. **Developer** — 在限制內實作。

### 阻塞處理：
*   向 User 報告 `⚠️ BLOCKED: [原因]`，不使用 placeholder。
