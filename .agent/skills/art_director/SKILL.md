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
2.  **Generation**: Use available tools (e.g., `generate_image` or local scripts in `tools/`) to create assets.
3.  **Review**: Verify the asset matches the `project_vibe.md` guidelines.
4.  **Integration**: Save the asset to `res/assets/` and import into Godot.

## Protocols
*   **Consistency**: Always compare new assets with existing ones in `res/assets/` to ensure style consistency.
*   **Naming**: Use `snake_case` for all asset filenames.
*   **Format**: Prefer `.png` for 2D assets.
