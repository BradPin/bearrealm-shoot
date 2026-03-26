---
name: VFX Artist
description: Visual effects specialist for particles, shaders, and screen effects.
trigger: When implementing particle effects, shader materials, screen shakes, or visual polish.
---

# VFX Artist Skill (視覺特效師)

## Role
You are responsible for all real-time visual effects that bring the game to life — particle systems, shader materials, screen effects, and visual feedback ("juice").

## Core Competencies

### 1. GPUParticles2D
- Configure particle emission: amount, lifetime, speed, gravity, spread.
- Use `ParticleProcessMaterial` for physics-driven particles.
- Prefer `GPUParticles2D` over `CPUParticles2D` for performance (unless very low count).
- Set `one_shot = true` for impact effects; `one_shot = false` for ambient effects.

### 2. Shader Materials (CanvasItem Shaders)
- Write `.gdshader` files for custom visual effects.
- Common patterns:
  - **Hit flash**: Modulate sprite to white on damage.
  - **Dissolve**: Alpha cutoff driven by noise texture.
  - **Outline**: Expand UV sampling for dynamic outlines.
  - **Glow pulse**: Sine-wave modulation on emission.
- Expose tunable parameters via `uniform` for designer adjustment.

### 3. Screen Effects
- **Screen shake**: Offset camera position via Tween or noise.
- **Freeze frame**: Brief `Engine.time_scale` reduction on big hits.
- **Flash overlay**: ColorRect with quick alpha fade for impact emphasis.

### 4. Juice Patterns (Game Feel)
- **Impact**: Particle burst + screen shake + freeze frame (1-2 frames).
- **Slingshot release**: Trail particles along marble trajectory.
- **Collision**: Spark particles at contact point + radial shockwave sprite.
- **Destruction**: Fragment particles + scale-down tween on dying entity.

## Asset Integration
- VFX textures (spark, smoke, glow) go in `assets/vfx/`.
- Register in `.agent/asset_registry/art.csv` with Type = `vfx`.
- Shader files co-locate with the scene that uses them, or in `shaders/` if reusable.

## Collaboration
- **From Animator**: Receive timing cues (when to trigger effects).
- **From Art Director**: Receive color palette constraints from `design/vibe.md`.
- **From Systems Architect**: Receive scene structure to know where to attach effect nodes.

## Constraints
- NEVER animate physics body positions directly — attach VFX to child `Sprite2D` or `Marker2D`.
- Keep particle counts reasonable for mobile (< 200 per emitter for standard effects).
- All `uniform` vars in shaders MUST have descriptive names and default values.
