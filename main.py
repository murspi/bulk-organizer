import argparse
from organizer import scan_directory

def main():
    parser = argparse.ArgumentParser(description="Bulk File Organizer")

    parser.add_argument("folder", help="Folder to organize")
    parser.add_argument("--dry-run", action="store_true", help="Simulate file moves")
    parser.add_argument("--mode", choices=["extension", "date"], default="extension", help="Sorting mode")

    args = parser.parse_args()

    try:
        scan_directory(args.folder, dry_run=args.dry_run, mode=args.mode)
    except Exception as e:
        print(f"Error {e}")

if __name__ == "__main__":
    main()