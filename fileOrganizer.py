import os
import shutil
from pathlib import Path

#Folder to organize
base_folder = Path.home() / "Downloads"

#define folders for each file type
folders = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".flv"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".sh", ".bat"]
}

#iterate over files in base_folder
for item in base_folder.iterdir():
    if item.is_file():
       ext = item.suffix.lower().lstrip('.')
       moved = False
       # Determine which category folder to use
       for folder, ext_list in folders.items():
           if ext in ext_list:
               dest_dir = base_folder / folder
               dest_dir.mkdir(exist_ok=True)
               item.rename(dest_dir / item.name)
               moved = True
               break
           #if extension didn't match any category, move to others
           if not moved:
                dest_dir = base_folder / "Others"
                dest_dir.mkdir(exist_ok=True)
                item.rename(dest_dir / item.name)