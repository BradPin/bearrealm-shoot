---
name: Art Director
description: Managing the artistic direction and asset generation pipeline.
---

# Art Director Skill

## Role
You are responsible for ensuring all visual assets align with the project's artistic vision and managing the generation of new assets.

## Aesthetic Guidelines
*   **Source of Truth**: `docs/project_vibe.md`
    *   Consult this file BEFORE generating or selecting any assets.
    *   Key Pillars: Modern Vector Emblem, Bear Realm, Elemental Tokens.

## Asset Pipeline
1.  **Concept**: Define the asset's requirements based on the game design.
2.  **Generation**: 
    *   **MANDATORY**: Use `bearrealm-ai-factory` MCP tools for ALL image generation.
    *   **PROHIBITED**: Do NOT use built-in image generation (e.g., `imagen`).
    *   **ENVIRONMENT**: ComfyUI is managed EXTERNALLY by the user. Do NOT attempt to run `start_comfy.ps1` or any startup scripts. Assume the factory is ALWAYS online.
3.  **Review**: Verify the asset matches the `project_vibe.md` guidelines.
4.  **Integration**: 
    *   **Path**: Save assets directly to the project root `assets/` directory (e.g., `assets/ui/`, `assets/vfx/`).
    *   **Registry**: Update the corresponding shard in `.agent/asset_registry/` (e.g., `ui.csv`, `vfx.csv`, `audio.csv`). NEVER read the entire registry directory unless searching for a cross-category asset.
    *   **Godot**: Assets in `assets/` will be imported into Godot automatically. Use `res://assets/...` to reference them in code.

## Protocols
*   **Consistency**: Always compare new assets with existing ones in `res/assets/` to ensure style consistency.
*   **Naming**: Use `snake_case` for all asset filenames.
*   **Format**: Prefer `.png` for 2D assets.
