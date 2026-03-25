# Asset Creation Workflow (SOP)

This workflow defines the strict process for Agent-driven asset generation (Art, Audio, UI elements) from conception to integration.

## 1. Vault Retrieval (Read Style)
*   **Art Assets**: ALWAYS read `.agent/design/vibe/master_art_prompt.md` before generating any images. Ensure the generated prompt adheres strictly to the defined visual style.
*   **Audio Assets**: ALWAYS read `.agent/design/vibe/master_audio_prompt.md` before generating any sound effects or BGM.

## 2. Generate Asset (via MCP)
*   **Tool**: Invoke the relevant MCP (e.g., ComfyUI, DALL-E, ElevenLabs, etc.) to generate the raw media.
*   **Naming**: Use strict `snake_case` (e.g., `sfx_fireball_hit_01.wav`, `icon_fire_sword_v1.png`).

## 3. Process Asset
*   **Images**: Run `python tools/asset_processor.py <path>` to remove background, crop, or slice sprite sheets as needed.
*   **Audio**: Ensure format is `.wav` or `.ogg` (Godot preferred formats). Trim silence if necessary.

## 4. Registry Logging (Mandatory)
*   Once the asset is successfully placed in the project directory, append an entry to `.agent/asset_registry.csv`.
*   Format: `Asset_ID,Type,Path,Status,Description`

## 5. Engine Integration
*   Load the asset into Godot (via `godot_bridge.py` or by directly assigning it to `.tscn` / `.tres` files if instructed).
*   Test the asset context (e.g., correct import settings: VRAM compression for 3D, Lossless for Pixel Art).