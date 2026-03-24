---
id: ISSUE-004
title: "[VFX] Particle System & Animation States"
status: TODO
tags: [vfx, animation, polishing]
primary_skill: developer
---
# [VFX] Particle System & Animation States

## Description
為彈珠碰撞加入視覺回饋，包含碰撞粒子效果與基於動量變化的 Squash & Stretch 動畫。

## Context
遊戲的打擊感來自於視覺回饋，彈珠在高速碰撞時應該有明顯的形變。

## Tasks
1. [ ] 建立 `CollisionVFX.tscn` (GPUParticles2D) 處理碰撞噴發效果。
2. [ ] 在 `PlayerMarble` 中加入 `AnimationPlayer` 處理變形動畫。
3. [ ] 實作代碼在碰撞瞬間觸發變形與粒子效果。
4. [ ] 針對不同陣營 (Elemental) 定義不同的粒子色調。

## Acceptance Criteria
- [ ] 碰撞時會產生朝向法線反方向的粒子。
- [ ] 彈珠在碰撞瞬間有明顯的縮放 (Squash) 效果並迅速恢復。
- [ ] 動畫流程平滑，無效能卡頓。
