# Art Reference Manifest

> SSOT for all curated reference images used by the `bearrealm-ai-factory` MCP.
> Agents MUST consult this file before calling `generate_game_asset`.

## How IPAdapter References Work

The MCP tool `generate_game_asset` uses **IPAdapter** to inject the visual style of a reference image into the generation process. This ensures consistent art style across all assets.

- **Auto-selection**: When `reference` is omitted, the tool picks the best match based on `asset_type` and `subject` keywords.
- **Manual override**: Pass `reference="subfolder/filename.png"` to use a specific image.

## Available References

### Characters (`characters/`)

| File | Use For | Auto-selected When |
|------|---------|-------------------|
| `characters/hunter.png` | All character sprites/portraits | `asset_type="character"` (default) |

### Icons (`icons/`)

| File | Use For | Auto-selected When |
|------|---------|-------------------|
| `icons/icon-ember.png` | Ember / Fire element icons | subject contains: fire, flame, ember |
| `icons/icon-aether.png` | Aether / Water element icons | subject contains: water, wave, aether, ice |
| `icons/icon-wild.png` | Wild / Wind element icons | subject contains: wind, leaf, wild, green, nature |
| `icons/icon-sanctum.png` | Sanctum / Earth element icons | subject contains: mountain, earth, sanctum, gold, shield, light |
| `icons/icon-umbral.png` | Umbral / Shadow element icons | subject contains: shadow, void, umbral, dark, purple |

### Marbles (`marbles/`)

| File | Use For | Auto-selected When |
|------|---------|-------------------|
| `marbles/yellow-ball.png` | Characters inside glass orbs | `asset_type="marble"` (default) |

### UI (`ui/`)

| File | Use For | Auto-selected When |
|------|---------|-------------------|
| `ui/ui-frame-1.png` | Stone UI panels/frames (rounded) | `asset_type="ui"` (default) |
| `ui/ui-frame-2.png` | Stone UI panels/frames (angular) | Manual: `reference="ui/ui-frame-2.png"` |

## Adding New References

1. Place the new image in the appropriate subfolder under `.agent/art_references/`.
2. Add an entry to this manifest.
3. If it should be auto-selected, add keyword mappings in `mcp_server.py` → `ICON_ELEMENT_REFS` dict.

## Example Calls

```python
# Auto-select (most common)
generate_game_asset(subject="ice dragon", asset_type="character")
# → uses characters/hunter.png automatically

# Auto-select with element matching
generate_game_asset(subject="fire flame", asset_type="icon")
# → matches "fire" keyword → uses icons/icon-ember.png

# Manual override for a specific style
generate_game_asset(subject="score panel", asset_type="ui", reference="ui/ui-frame-2.png")
```
