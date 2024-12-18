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
