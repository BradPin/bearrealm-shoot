---
name: Art Director
description: Dispatch hub for art generation and style review.
---

# Art Director Skill

## Role
Ensure all visual assets align with the project's artistic vision.

## Quick Rules
- **MANDATORY**: Use `bearrealm-ai-factory` MCP → `generate_game_asset` for ALL image generation.
- **PROHIBITED**: Built-in image generation (e.g., `imagen`). Do NOT start ComfyUI.
- **Output path**: `assets/art/{type}/`, snake_case `.png` filenames.
- **"Bear"** = stout round-bodied human men (bear community), NOT literal animals.

## On-Demand Sub-docs (read ONLY when needed)

| When | Read |
|------|------|
| Generating an asset | `.agent/art_references/manifest.md` — available reference images and MCP tool usage |
| Writing/reviewing prompts | `.agent/design/vibe/master_art_prompt.md` — prompt templates per asset type |
| Reviewing overall art direction | `design/vibe.md` — high-level style pillars and faction palettes |
| Updating asset registry | `.agent/asset_registry/{type}.csv` |
