import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image

# Initialize tkinter
root = tk.Tk()
root.withdraw()  # Hide the main window

# Ask user to select a folder
folder_selected = filedialog.askdirectory(title="Select a Base Folder")

if not folder_selected:
    print("No folder selected. Exiting.")
    exit()

# Supported image file extensions
image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']

def is_image_file(filename):
    """Check if a file is an image based on its extension."""
    return any(filename.lower().endswith(ext) for ext in image_extensions)

def rename_images_in_folder(folder_path):
    """Rename all image files in the given folder according to the folder name and a number."""
    folder_name = os.path.basename(folder_path)
    count = 1

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path) and is_image_file(filename):
            # Generate new file name
            extension = os.path.splitext(filename)[1]
            new_filename = f"{folder_name}-{count}{extension}"
            new_file_path = os.path.join(folder_path, new_filename)
            
            # Rename the file
            os.rename(file_path, new_file_path)
            print(f"Renamed: {file_path} -> {new_file_path}")
            count += 1

# Traverse all folders and subfolders
for root_folder, subdirs, files in os.walk(folder_selected):
    rename_images_in_folder(root_folder)

print("All images have been renamed.")
