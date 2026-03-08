from pathlib import Path
from operations import create_folder, move_file
import datetime

def scan_directory(folder_path: str, dry_run: bool = False, mode: str = "extension"):
    """
    Scan a directory and organize files by extension or date.

    Parameters:
        folder_path (str): path to directory
        dry_run (bool): simulate file moves
        mode (str): grouping mode ("extension" or "date")
    """
    path = Path(folder_path)

    if not path.exists():
        raise FileNotFoundError(f"{folder_path} does not exist")
    
    if not path.is_dir():
        raise NotADirectoryError(f"{folder_path} is not a directory")

    files_by_group = {}
    
    for item in path.iterdir():

        if item.is_dir():
            continue

        if mode == "extension":
            key = item.suffix.lower()

        elif mode == "date":
            timestamp = item.stat().st_mtime
            key = str(datetime.datetime.fromtimestamp(timestamp).year)

        if key not in files_by_group:
            files_by_group[key] = []

        files_by_group[key].append(item)

    print("\nFiles detected:")

    for group, files in files_by_group.items():
        name = group if group else "[no extension]"
        print(f"{name}: {len(files)} files")

    for group, files in files_by_group.items():

        if mode == "extension":
            folder_name = group[1:] if group else "no_extension"
        else:
            folder_name = group

        target_folder = create_folder(path, folder_name)

        for file in files:
            move_file(file, target_folder, dry_run)