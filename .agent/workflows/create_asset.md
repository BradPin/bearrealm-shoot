---
description: Create a new game asset (image), process it, and integrate it into Godot.
---

# Asset Creation Workflow

This workflow guides the Agent to generate visual assets using internal tools and process them for Godot.

## 1. Analyze & Refine Prompt
*   **Source**: Read `docs/project_vibe.md` to ensure style consistency (Vector Emblem, Heroic Cartoon, etc.).
*   **Context**: Identify the asset type (Icon, Character, Prop).

## 2. Generate Image
*   **Tool**: Use `generate_image`.
*   **Naming**: Use `snake_case` for the filename (e.g., `fire_sword_v1`).
*   **Prompting**: Apply the style keywords from `project_vibe.md`.

## 3. Process Asset
*   **Action**: Remove background and resize.
*   **Command**:
    ```bash
    d:/workspace/bearrealm-shoot/.venv/Scripts/python.exe tools/asset_processor.py res/assets/[filename].png --resize 512x512
    ```
    *(Adjust resize dimensions if it's an icon vs character)*

## 4. Integrate (Optional)
*   **If replcing existing asset**:
    *   Use `update_scene_resource` (via `godot_bridge.py`) if the user requests replacing a specific reference in a scene.
*   **Import**:
    *   Run Godot import if necessary (usually automatic on window focus, but can be forced via headless command if needed).

## 5. Verify
*   **Check**: Confirm files exist in `res/assets/`.
*   **Notify**: Inform the user of the generated files.
