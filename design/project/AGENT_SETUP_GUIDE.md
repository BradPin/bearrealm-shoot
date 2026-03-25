# 🛠️ Agent-Driven 遊戲專案：使用者手動配置指南 (User Setup Guide)

這份文件記錄了為了讓 Agent 真正能夠「自動生圖、生音效」並「優化 Token 讀取」，身為專案管理者的您需要進行的**手動設定工作流程**與**相關資源估算**。

---

## 步驟 1：定義「提示詞金庫 (Prompt Vault)」(免費, 需要創意)

Agent 需要一個絕對的「風格指引」，避免每次生成的圖示或音效風格突兀。

*   **動作**：請打開以下檔案，將裡面的 `[USER_TODO: ...]` 替換成您腦中的真實設定。
    *   👉 `.agent/design/vibe/master_art_prompt.md` (定義視覺風格、色系)
    *   👉 `.agent/design/vibe/master_audio_prompt.md` (定義音效風格、節奏)
*   **建議**：描述越精準越好，例如 "Cel-shaded, like Hades but with bears, thick black outlines, neon pink highlights."。

---

## 步驟 2：掛載多媒體生成 MCP (Model Context Protocol) (需外部資源/付費)

目前 Agent 本身只會打字與修改程式碼，若要讓它「憑空產出素材」，您必須在 IDE / Agent 環境配置中 (`mcp.json` 或類似設定) 掛載相關的生圖/生音效 Server。

### A. 圖像生成 MCP (選一即可)
Agent 透過這類 MCP 下達指令，Server 產生圖片後儲存到專案目錄。

1.  **DALL-E 3 MCP (建議，最易上手)**
    *   **資源**：需要一個 [OpenAI API Key](https://platform.openai.com/api-keys)。
    *   **花費**：依使用量計費，標準解析度每張圖約 $0.04 USD。
    *   **實作方式**：尋找開源的 `mcp-openai-dalle` 伺服器並加入 `mcp.json`。
2.  **ComfyUI / Stable Diffusion MCP (進階，風格最一致)**
    *   **資源**：一台有強大 GPU 的本機電腦，或雲端運算資源。本機需安裝 ComfyUI。
    *   **花費**：本機免費 (電費)；若用雲端 API (如 Replicate) 則依秒數計費。
    *   **實作方式**：撰寫或尋找將 ComfyUI API 包裝成 MCP Server 的腳本，讓 Agent 可以直接觸發 ComfyUI Workflow (例如：文生圖 + 去背)。

### B. 音效/音樂生成 MCP (選一即可)
1.  **ElevenLabs MCP (適合 SFX 與語音)**
    *   **資源**：[ElevenLabs API Key](https://elevenlabs.io/)。
    *   **花費**：有免費額度 (10,000 字元/月)，付費版從 $5 USD/月 起跳。
2.  **Suno / Udio API 封裝 (適合 BGM)**
    *   **資源**：這類平台通常沒有直接開放完美的官方 API，需尋找社群封裝的開源 MCP 工具。
    *   **提示**：若覺得整合太複雜，音效部分您可以保留為「半自動」（Agent 寫好 Prompt，您手動去網頁產生後丟進專案）。

---

## 步驟 3：擴充資產處理工具 `tools/asset_processor.py` (可與 Agent 協作)

有了生圖能力後，生成的圖片通常會有背景或尺寸不對，需要腳本自動處理。

*   **動作**：確認 `tools/asset_processor.py` 是否具備以下能力 (如果沒有，可以要求 Agent 幫您用 Python 實作)：
    1.  **Image Resize / Crop** (利用 `Pillow` 函式庫)。
    2.  **Background Removal** (利用開源的 `rembg` 函式庫，非常適合遊戲素材去背)。
*   **花費**：免費 (Python 本機執行)。

---

## 步驟 4：Godot 場景輕量化機制 (Blueprint Pattern) (可與 Agent 協作)

為避免 Agent 每次修改介面或動畫時讀取龐大的 `.tscn` 而耗盡 Token，我們需要一個「場景快照」機制。

*   **動作**：指示 Agent 擴充您的 `tools/sync_context.py`。
*   **目標**：每次您存檔 Godot 專案時，腳本自動掃描 `scenes/` 目錄下的 `.tscn`，並將結構精簡輸出為 Markdown 放到 `.agent/scene_blueprints/` 下。
    *   *例如：只需要知道 `VBoxContainer` 底下有兩個 `Button`，而不需要知道這兩個 `Button` 的字型顏色十六進位碼與邊界值。*

---

## ✅ 啟動後的開發循環

當上述設定完成後，您可以對 Agent 下達這類指令：
> *"幫我實作一個火屬性怪物的打擊特效與音效，並把它加進目前的戰鬥場景中。"*

**Agent 預期的行為：**
1. 讀取 `master_art_prompt.md` & `master_audio_prompt.md`。
2. 呼叫生圖 MCP 生產「火花特效圖檔」；呼叫音效 MCP 生產「爆炸聲 .wav」。
3. 呼叫 `asset_processor.py` 將特效圖檔去背、裁切。
4. 將資訊寫入 `.agent/asset_registry.csv`。
5. 進入 Godot 專案，新增 `AudioStreamPlayer2D` 與 `GPUParticles2D` 節點。
6. 修改相關的 GDScript 觸發邏輯。