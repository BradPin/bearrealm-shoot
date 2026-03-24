---
id: ISSUE-005
title: "[Pipeline] AI-Driven Marble Unit Generator"
status: TODO
tags: [tools, ai, assets]
primary_skill: art_director
---
# [Pipeline] AI-Driven Marble Unit Generator

## Description
建立一套自動化工具，將企劃描述轉化為 Godot 場景資產。

## Context
使用者不具備美術製作能力，需依賴 Agent 處理從生成圖片到封裝場景的全流程。

## Tasks
1. [ ] 優化 `tools/asset_processor.py` 整合 `rembg` 去背功能。
2. [ ] 實作 `tools/marble_generator.py`：
    - 調用 `generate_image` 生成頭像。
    - 套用圓形遮罩與陣營邊框。
    - 自動產生對應的 `.tscn` 檔案。
3. [ ] 更新 `Art Director` Skill 以支持此自動化流程。

## Acceptance Criteria
- [ ] 一個指令即可生成完整的彈珠場景檔案。
- [ ] 生成的圖片自動去背且符合 512x512 規範。
- [ ] `.tscn` 檔案結構正確，包含 `Sprite2D` 且已正確對齊中心。
