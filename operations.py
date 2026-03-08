from pathlib import Path

def create_folder(base_path: Path, folder_name: str) -> Path:
    target_folder = base_path / folder_name
    target_folder.mkdir(exist_ok=True)
    return target_folder

def move_file(file: Path, destination_folder: Path, dry_run: bool = False):
    destination = destination_folder / file.name
    
    if destination.exists():
        print(f"Skipping (already exists): {destination.name}")
        return
    if dry_run:
        print(f"[DRY-RUN] Would move: {file} -> {destination}")
    else:
        file.rename(destination)
        print(f"Moved: {file.name} -> {destination_folder.name}/")