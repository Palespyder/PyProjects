# Image Renaming Tool

This Python script renames image files in a selected folder and its subfolders. The new names are generated based on the folder name and a sequential number. The tool supports multiple image file formats and uses Tkinter for a graphical folder selection.

## Features

- Select a folder through a graphical user interface.
- Renames image files in the selected folder and its subfolders.
- Supports common image file formats including JPG, PNG, GIF, BMP, and TIFF.
- New filenames are based on the folder name and a sequential number.

## Requirements

- Python 3.x
- Tkinter (included with Python standard library)
- Pillow (Python Imaging Library, installable via pip)

## Installation

1. Ensure Python 3.x is installed on your system.
2. Install Pillow if it is not already installed:
    ```bash
    pip install Pillow
    ```

## Usage

1. Run the script:
    ```bash
    python rename_images.py
    ```
2. A file dialog will appear prompting you to select a folder.
3. The script will rename all image files in the selected folder and its subfolders based on the folder name and a sequential number.

## Code Explanation

- **Imports**:
  - `os`: Provides functions to interact with the operating system, such as file path manipulation and renaming files.
  - `tkinter as tk`: Used for creating a simple graphical user interface to select the folder.
  - `filedialog` from `tkinter`: Used to open a file dialog for selecting a folder.
  - `Image` from `PIL`: Imported but not used in this script.

- **Functions**:
  - `is_image_file(filename)`: Checks if a file has an image file extension.
  - `rename_images_in_folder(folder_path)`: Renames image files in the specified folder.

- **Main Execution**:
  - Initializes a Tkinter window (hidden) to select a folder.
  - Iterates through the selected folder and its subfolders, renaming image files.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

Created by [Your Name].

## Acknowledgements

- Pillow for image processing capabilities.
- Tkinter for the graphical user interface.

For any issues or contributions, please open an issue or submit a pull request on the [GitHub repository](https://github.com/yourusername/yourrepository).
