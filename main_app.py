import os
import shutil
from pathlib import Path
import json
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

def load_config(config_file="config.json"):
    with open(config_file, "r") as file:
        return json.load(file)

FILE_TYPE_FOLDERS = load_config()

def organize_desktop(desktop_path):
    print(f"Organizing files in {desktop_path}...")

    # Iterate over files in the desktop folder
    for item in os.listdir(desktop_path):
        item_path = os.path.join(desktop_path, item)

        # Skip directories
        if os.path.isdir(item_path):
            continue

        # Identify file extension
        _, file_extension = os.path.splitext(item)

        # Determine the target folder
        target_folder = None
        for folder, extensions in FILE_TYPE_FOLDERS.items():
            if file_extension.lower() in extensions:
                target_folder = folder
                break

        if not target_folder:
            target_folder = "Others"

        # Create target folder if it doesn't exist
        target_folder_path = os.path.join(desktop_path, target_folder)
        os.makedirs(target_folder_path, exist_ok=True)

        # Move the file
        new_file_path = os.path.join(target_folder_path, item)
        if os.path.exists(new_file_path):
            # Handle file conflict by renaming
            base, ext = os.path.splitext(item)
            new_file_path = os.path.join(target_folder_path, f"{base}_copy{ext}")

        shutil.move(item_path, new_file_path)
        print(f"Moved: {item} -> {target_folder}")
