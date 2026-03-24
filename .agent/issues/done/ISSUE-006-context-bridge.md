---
id: ISSUE-006
title: "[Context] Godot MCP & Documentation Bridge"
status: TODO
tags: [mcp, infrastructure, cursor]
---
# [Context] Godot MCP & Documentation Bridge

## Description
配置 `godot-mcp` 並建立檔案化的專案 Context 供 Cursor 與其他 AI 工具讀取。

## Context
確保跨 AI 環境 (Antigravity & Cursor) 的開發一致性，避免重複解釋專案規範。

## Tasks
1. [ ] 在 Antigravity 環境配置 `godot-mcp` (Coding-Solo)。
2. [ ] 實作 `tools/sync_context.py` 匯出 `Input Map` 與 `Collision Layers`。
3. [ ] 建立 `docs/godot_guidelines.md` 強制執行 Typed GDScript 規範。

## Acceptance Criteria
- [ ] Agent 能透過 MCP 指令 `godot:get_scene_tree` 讀取場景。
- [ ] 專案設定摘要檔案能自動更新。
- [ ] Cursor 能讀取到專案專屬的類型定義與腳本類別。
