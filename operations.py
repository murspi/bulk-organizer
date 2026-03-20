from pathlib import Path
from logger_config import setup_logger

logger = setup_logger()

def create_folder(base_path: Path, folder_name: str) -> Path:
    target_folder = base_path / folder_name
    target_folder.mkdir(exist_ok=True)
    return target_folder

def move_file(file: Path, destination_folder: Path, dry_run: bool = False):
    destination = destination_folder / file.name
    
    if destination.exists():
        logger.info("Moved: %s -> %s", file.name, destination_folder.name)
        return
    if dry_run:
        logger.info("[DRY-RUN] Would move: %s -> %s", file, destination)
    else:
        file.rename(destination)
        logger.warning("Skipping (already exists): %s", destination.name)