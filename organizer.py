from pathlib import Path
from operations import create_folder, move_file
from logger_config import setup_logger
from typing import Optional
import datetime

logger = setup_logger()

def scan_directory(folder_path: str, dry_run: bool = False, mode: str = "extension", recursive: bool = False, limit: Optional[int] = None):
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
    
    if recursive:
        logger.info("Recursive mode enabled. Scanning subdirectories.")
        items = path.rglob("*")
    else:
        logger.info("Scanning only top-level directory.")
        items = path.iterdir()

    for item in items:
        if item.is_dir():
            continue

        if mode == "extension":
            key = item.suffix.lower()
        elif mode == "date":
            timestamp = item.stat().st_mtime
            key = str(datetime.datetime.fromtimestamp(timestamp).year)

        files_by_group.setdefault(key, []).append(item)

    if limit is not None:
        logger.info("Limiting processing to %d files", limit)

        all_files = [(group, file) for group, files in files_by_group.items() for file in files]

        limited_files = all_files[:limit]

        files_by_group = {}
        for group, file in limited_files:
            files_by_group.setdefault(group, []).append(file)

    logger.info("Files detected:")

    for group, files in files_by_group.items():
        name = group if group else "[no extension]"
        logger.info("%s: %d files", name, len(files))

    for group, files in files_by_group.items():

        if mode == "extension":
            folder_name = group[1:] if group else "no_extension"
        else:
            folder_name = group

        target_folder = create_folder(path, folder_name)

        for file in files:
            move_file(file, target_folder, dry_run)

def undo_sorting(folder_path: str, dry_run: bool = False):
    """Undo the organization by moving files back to the main folder
    and removing empty subfolders."""

    path = Path(folder_path)

    if not path.exists():
        raise FileNotFoundError(f"{folder_path} does not exist")
    
    if not path.is_dir():
        raise NotADirectoryError(f"{folder_path} is not a directory")
    
    logger.info("Undo mode activated. Restoring files to the main folder.")

    for subfolder in path.iterdir():
        if not subfolder.is_dir():
            continue 

        logger.info("Processing folder: %s", subfolder.name)

        for file in subfolder.iterdir():
            if file.is_file():
                target = path / file.name
                logger.info("Restoring %s -> %s", file.name, target)

                if not dry_run:
                    file.rename(target)

        if not any(subfolder.iterdir()):
            logger.info("Removing empty folder: %s", subfolder.name)
            if not dry_run:
                subfolder.rmdir()

    logger.info("Undo complete.")