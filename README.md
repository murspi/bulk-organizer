# Bulk File Organizer (CLI Tool)

A command‑line utility for organizing files in a folder by **extension** or **creation year**, with support for **recursive scanning**, **dry‑run mode**, **global file limits**, and a full **undo** feature that restores files back to their original folder.

This tool is designed for automation, clarity, and safety — no files are overwritten, and all operations are logged.

---

## Features

- Organize files by **extension** (e.g., `jpg/`, `txt/`, `pdf/`)
- Organize files by **year** (e.g., `2023/`, `2024/`)
- **Undo mode** to restore files back to the main folder
- **Recursive** directory scanning (`--recursive`)
- **Dry‑run** mode (`--dry-run`) to preview actions
- **Limit** the total number of files processed (`--limit`)
- Safe operations:
  - No overwriting existing files
  - Skips duplicates with warnings
  - Removes empty folders during undo
- Clean logging output for every action

---

## Installation

Clone the repository:

```bash
git clone https://github.com/murspi/bulk-organizer.git
cd bulk-organizer
