import argparse
from organizer import scan_directory, undo_sorting
from logger_config import setup_logger

logger = setup_logger()

def main():
    parser = argparse.ArgumentParser(description="Bulk File Organizer")

    parser.add_argument("folder", help="Folder to organize")
    parser.add_argument("--dry-run", action="store_true", help="Simulate file moves")
    parser.add_argument("--mode", choices=["extension", "date"], default="extension", help="Sorting mode")
    parser.add_argument("--recursive", action="store_true", help="Scan subdirectories recursively")
    parser.add_argument("--limit", type=int, default=None, help="Limit the number of files to process")
    parser.add_argument("--undo", action="store_true", help="Undo previous organization and restore files to the main folder")

    args = parser.parse_args()

    try:
        if args.undo:
            undo_sorting(args.folder, dry_run=args.dry_run)
        else:
            scan_directory(args.folder, dry_run=args.dry_run, mode=args.mode, recursive=args.recursive, limit=args.limit)
    except Exception as e:
        logger.error("Error occurred: %s", e)

if __name__ == "__main__":
    main()