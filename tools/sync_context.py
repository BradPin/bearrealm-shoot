import os
import re
from pathlib import Path

def sync_context():
    project_root = Path(__file__).parent.parent
    godot_file = project_root / "project.godot"
    output_file = project_root / ".agent/godot_index.md"

    if not godot_file.exists():
        print("Error: project.godot not found!")
        return

    with open(godot_file, "r", encoding="utf-8") as f:
        content = f.read()

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("# Godot Project Context (Auto-generated)\n\n")
        f.write("> 此檔案由 `tools/sync_context.py` 自動生成，提供 AI (Cursor/Antigravity) 讀取專案設定。\n\n")

        # Basic Info
        f.write("## 1. 專案基本資訊\n")
        name = re.search(r'config/name="(.*?)"', content)
        f.write(f"*   **專案名稱**: {name.group(1) if name else 'Unknown'}\n")
        
        main_scene = re.search(r'run/main_scene="(res://.*?)"', content)
        f.write(f"*   **主場景**: {main_scene.group(1).strip() if main_scene else 'Not set'}\n\n")

        # Collision Layers
        f.write("## 2. 碰撞層級 (2D Physics Layers)\n")
        layer_section = re.findall(r'2d_physics/layer_(\d+)="(.*?)"', content)
        if layer_section:
            for layer_num, layer_name in layer_section:
                f.write(f"*   Layer {layer_num}: `{layer_name}`\n")
        else:
            f.write("*   *目前尚未定義自定義層級名稱。*\n")
        f.write("\n")

        # Input Map
        f.write("## 3. 輸入映射 (Input Map)\n")
        # Extract keys from [input] section until next section [
        input_match = re.search(r'\[input\](.*?)(\n\[|$)', content, re.DOTALL)
        if input_match:
            input_section = input_match.group(1)
            actions = re.findall(r'^(\w+)=\{', input_section, re.MULTILINE)
            for action in actions:
                f.write(f"*   Action: `{action}`\n")
        else:
            f.write("*   *目前尚未定義自定義輸入事件。*\n")

    print(f"Success: Updated {output_file}")

if __name__ == "__main__":
    sync_context()
