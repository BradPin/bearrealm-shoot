Write-Host "Starting Bearrealm AI Factory (ComfyUI)..." -ForegroundColor Cyan
cd D:\workspace\bearrealm-ai-factory
# Use uv run to ensure the correct environment is used automatically
uv run python ComfyUI/main.py
