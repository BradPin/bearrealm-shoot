import os
import sys
import shutil
from pathlib import Path

def manage_task(command, task_id=None):
    project_root = Path(__file__).parent.parent
    todo_dir = project_root / ".agent/issues/todo"
    progress_dir = project_root / ".agent/issues/in_progress"
    done_dir = project_root / ".agent/issues/done"
    overview_file = project_root / ".agent/overview.md"

    if command == "start" and task_id:
        # Move todo -> in_progress
        for f in todo_dir.glob(f"ISSUE-{task_id}*"):
            new_path = progress_dir / f.name
            shutil.move(str(f), str(new_path))
            print(f"Task Started: {f.name}")
            # Update Overview Current Focus
            update_overview_focus(overview_file, f.name)
            return

    if command == "finish" and task_id:
        # Move in_progress -> done
        for f in progress_dir.glob(f"ISSUE-{task_id}*"):
            new_path = done_dir / f.name
            shutil.move(str(f), str(new_path))
            print(f"Task Finished: {f.name}")
            update_overview_focus(overview_file, "Waiting for next instruction...")
            return

def update_overview_focus(file_path, task_name):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    with open(file_path, "w", encoding="utf-8") as f:
        for line in lines:
            if "Current Focus" in line:
                f.write(f"*   **Current Focus**: {task_name}\n")
            elif "待辦核心任務" in line:
                # Add a marker that we are in task mode
                f.write(line)
            else:
                f.write(line)

if __name__ == "__main__":
    if len(sys.argv) > 2:
        manage_task(sys.argv[1], sys.argv[2])
    else:
        print("Usage: python task_manager.py [start|finish] [ID]")
