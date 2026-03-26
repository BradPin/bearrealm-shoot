# Project Context: Bearrealm Shoot

## Project Overview
`bearrealm-shoot` 是一個基於「熊域 (Bearrealm)」世界觀的類怪物彈珠 (Slingshot Battle) 2D 遊戲。
*   **引擎**: Godot 4.4.1 (Forward Plus)。
*   **語言**: Typed GDScript (強制強型別)。
*   **核心玩法**: 透過拉動彈珠進行碰撞戰鬥。
*   **目前狀態**: 專案初始化完成，環境 MCP 配置完成。正進入原型開發期 (Prototype Phase)。

## 最近里程碑
- [x] 專案基礎環境設定 (Godot 4.4 + VS Code/Antigravity)。
- [x] 配置 `godot-mcp` 與同步工具。
- [x] 確立「Slingshot」核心玩法與物理技術選型。

## 🤖 Agent Instructions (CRITICAL)
1.  **Strict Typing**: 所有 GDScript 必須標註類型。
2.  **Doc Reference**: 代碼風格參考 `.agent/guidelines.md`，Godot 設定參考 `.agent/godot_index.md`。
3.  **Design Flow**: 讀取 `design/game/` 的企劃後，主動在 `design/` 生成結構化文件。
4.  **Skill Dispatch**: 參照 `.agent/rules.md` 的 Skill Dispatcher 進行角色路由。
5.  **Collaboration**: 多步驟任務遵循 `.agent/protocols/inter_agent.md` 的協作流。

## 待辦核心任務
- [ ] ISSUE-003: 核心彈射物理 (Current Focus)。
- [ ] ISSUE-004: 碰撞特效與動畫。
- [ ] ISSUE-005: AI 美術管線。
