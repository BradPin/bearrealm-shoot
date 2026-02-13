---
id: ISSUE-003
title: Implement Image Generation Tool
status: TODO
tags: [tools, python, pipeline]
---
# Implement Image Generation Tool

## Description
Create or finalize the `tools/generate_icon.py` script to standardize the asset generation process.

## Context
A `tools/generate_icon.py` script was referenced but not found on disk. This tool should wrap the image generation logic (or interface with the `generate_image` tool) to produce consistent assets based on the project's art style.

## Tasks
1.  Create `tools/generate_icon.py`.
2.  Implement logic to:
    - Accept parameters (timestyle, element, type).
    - Construct prompts based on `docs/project_vibe.md`.
    - (Optional) Call `generate_image` or provide a template for manual generation.
3.  Ensure the script can be run via `run_command`.

## Acceptance Criteria
- [ ] `tools/generate_icon.py` exists and is executable.
- [ ] The script can generate or prompt for an icon consistent with the project vibe.
- [ ] Usage instructions are added to the script header.
