import argparse
import os
import sys
import re

def update_resource(file_path, target_var, new_value):
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} not found.")
        sys.exit(1)
        
    print(f"Updating {file_path}: Setting {target_var} to {new_value}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Logic for .gd files
        if file_path.endswith('.gd'):
            # Look for: var texture_path = "old_value" OR @export var texture = preload("...")
            # Simple regex for string assignment
            # Pattern: var variable_name = "..."
            pattern = f'(var\\s+{re.escape(target_var)}\\s*=\\s*)"[^"]*"'
            replacement = f'\\1"{new_value}"'
            
            # Pattern for preload: preload("...")
            if 'preload' in content:
                 pattern_preload = f'(var\\s+{re.escape(target_var)}\\s*=\\s*preload\\()"([^"]*)"\\)'
                 replacement_preload = f'\\1"{new_value}")'
                 content = re.sub(pattern_preload, replacement_preload, content)

            new_content = re.sub(pattern, replacement, content)
            
        # Logic for .tscn files
        elif file_path.endswith('.tscn'):
            # Text resource format is complex, but often properties are:
            # texture = ExtResource("1_xxxxx")
            # OR explicit path
            # For now, let's assume we are replacing a specific string value if found, 
            # OR we might need to handle ExtResource IDs.
            # Simplified approach: If the user passes a specific property line to match
            
            # If target_var is a property name like 'texture', we look for 'texture = ...'
            # Note: This is fragile without a real parser.
            pattern = f'({re.escape(target_var)}\\s*=\\s*)"[^"]*"' # for direct string props
            replacement = f'\\1"{new_value}"'
            
            # Also handle Load path if target is a resource path
            # [ext_resource path="res://..." type="Texture2D" id="..."]
            # if target_var is the old path, replace with new path
            if target_var.startswith("res://"):
                 new_content = content.replace(target_var, new_value)
            else:
                 new_content = re.sub(pattern, replacement, content)
                 
        else:
            print("Unsupported file type")
            sys.exit(1)
            
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print("File updated successfully.")
        else:
            print("No changes made (pattern not found).")
            
    except Exception as e:
        print(f"Error updating resource: {e}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Update Godot resource references')
    parser.add_argument('file', type=str, help='Target .tscn or .gd file')
    parser.add_argument('variable', type=str, help='Variable name or Old Path to replace')
    parser.add_argument('value', type=str, help='New value or New Path')
    
    args = parser.parse_args()
    update_resource(args.file, args.variable, args.value)
