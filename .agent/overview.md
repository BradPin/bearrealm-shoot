# Project Context: Bearrealm Shoot

## Project Overview
`bearrealm-shoot` 是一個使用 Godot Engine (v4.4.1) 開發的遊戲專案。
*   **類型**: 射擊遊戲 (具體玩法待定義)。
*   **引擎**: Godot 4.4.1 (Forward Plus Renderer)。
*   **語言**: GDScript。
*   **關聯專案**: 繼承自 `bearrealm-clash` 的開發規範與環境設定。

## Current Status
*   **專案初始化**: 完成。
*   **基礎設定**: 已同步 `.editorconfig`, `.gdlintrc`, VS Code 設定 (`launch.json`, `tasks.json`)。
*   **目錄結構**: 基礎 Godot 結構已建立。

## Key Directories
*   `scenes/`: 存放遊戲場景檔案 (.tscn)。
*   `assets/`: 存放美術與音效素材。
*   `.vscode/`: 編輯器與除錯設定。
*   `interface/`: (預留) UI 相關邏輯。
*   `domain/`: (預留) 核心遊戲邏輯與資料層。

---

## 🤖 Agent Instructions (CRITICAL)
**致所有參與此專案的 AI Agent：**

1.  **Read First**: 在開始任何複雜任務前，請閱讀此檔案以了解專案當前狀態與全貌。
2.  **Actively Update**: 當你完成了以下變更時，**必須**主動更新此檔案：
    *   實作了新的核心功能 (例如：完成角色移動、新增敵人系統)。
    *   改變了專案的架構或目錄結構。
    *   新增了重要的設定或插件 (Addons)。
    *   確立了新的遊戲機制規則。
3.  **Maintain Clarity**: 保持內容簡潔清晰，這是專案的高層次地圖，而非程式碼細節。
