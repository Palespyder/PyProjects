# File Organizer Tool

This Python script organizes files in a selected folder into subfolders based on their file types (extensions). It uses Tkinter for graphical folder selection and creates separate folders for each file type.

## Features

- Select a folder through a graphical user interface.
- Organizes files by creating subfolders based on file extensions.
- Handles name conflicts by renaming files with duplicate names.
- Supports various file types and skips hidden/system files.

## Requirements

- Python 3.x
- Tkinter (included with Python standard library)
- No additional external libraries required

## Installation

1. Ensure Python 3.x is installed on your system.

## Usage

1. Run the script:
    ```bash
    python organize_files.py
    ```
2. A file dialog will appear prompting you to select a folder.
3. The script will organize files in the selected folder into subfolders named after their file types (e.g., `JPG_FILES`, `PNG_FILES`).

## Code Explanation

- **Imports**:
  - `os`: Provides functions for interacting with the operating system, such as file path manipulation and folder creation.
  - `shutil`: Used for moving files from one location to another.
  - `tkinter as tk`: Used to create a simple graphical user interface for folder selection.
  - `filedialog` from `tkinter`: Opens a file dialog for selecting a folder
