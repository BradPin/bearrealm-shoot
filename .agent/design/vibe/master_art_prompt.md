# Master Art Prompt Vault

> Foundational style guidelines and prompt templates for all AI-generated assets.
> **AGENT DIRECTIVE**: Always use the matching template for the asset_type. Never freestyle prompts.

## Global Style Keywords (inject into EVERY prompt)

```
STYLE_CORE = "stylized 2D game art, cartoon fantasy illustration, Hearthstone Supercell art style"
STYLE_RENDERING = "bold clean outlines, smooth painted shading, warm saturated colors, soft rim lighting"
STYLE_QUALITY = "professional game asset, polished mobile game quality, masterpiece"
```

## Prompt Templates

### 1. Character (Portraits / Full-body Sprites)

**Base Prompt**: `stylized 2D game character art, cartoon fantasy illustration, [Subject], chubby stout proportions, bold clean dark brown outlines, smooth painted shading, warm saturated colors, earthy brown and gold palette, soft rim lighting, Hearthstone Supercell card art style, full body, centered, plain white background, no text, professional game asset, masterpiece`

**Notes**: "Bear" = stout round-bodied human men (bear community aesthetic), NOT literal animals. Characters should have chubby/stocky body types. Warm earth tones as base. Bold visible outlines are critical for the game art look.

### 2. Icon (Elemental Medallions / Tokens)

**Base Prompt**: `hand-painted game element icon, large bold [Subject] symbol on a round warm gray stone disc, thick dark gray border ring, subtle stone texture, warm muted tones, stylized fantasy game art, simple centered composition, single round token, white background, no text, no shadow, masterpiece`

**Notes**: IPAdapter ref=icon-ember.png handles style. Prompt emphasizes warmth, stone texture, large centered symbol. Icons render at 512x512. CRITICAL negative additions for icon: "person, human, character, face, body, portrait, animal, 3d render, metallic, glossy, shiny, ornate, complex, multiple objects, long shadow, drop shadow, flat design, material design"

### 3. Marble (Character inside Sphere)

**Base Prompt**: `stylized 2D game art, cartoon fantasy illustration, [Subject] trapped inside a glowing translucent glass orb, chubby stout proportions, bold clean dark outlines, warm golden glow, juicy glass reflections and highlights, smooth painted shading, Hearthstone Supercell art style, transparent background, centered, professional game asset, masterpiece`

**Notes**: The sphere should feel glossy and translucent. Character inside uses same stout proportions as character type.

### 4. UI Frame (Panels / Borders)

**Base Prompt**: `stylized 2D game UI panel, [Subject], carved stone frame, dark gray stone border with lighter stone center, bold dark outlines, subtle stone cracks and texture, cartoon fantasy game style, warm muted earth tones, simple clean design, no character, white background, professional game UI asset, masterpiece`

**Notes**: UI frames use stone/slate material. Dark borders, lighter interior, clean game UI aesthetic.

## Negative Prompt (Mandatory — use for ALL types)

```
realistic, photorealistic, photo, semi-realistic, hyperrealistic, 3d render, 3d sculpted, anime, manga, cel-shaded, pixel art, blurry, grainy, noisy, low quality, low resolution, watermark, text, words, letters, signature, deformed, ugly, disfigured, extra limbs, bad anatomy, bad proportions, oversaturated neon colors, sketchy messy lines, heavy impasto texture, abstract, minimalist, dark moody lighting, ornate border, complex frame
```
