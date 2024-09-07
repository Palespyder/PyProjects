import os
import shutil
import tkinter as tk
from tkinter import filedialog

# Initialize tkinter
root = tk.Tk()
root.withdraw()  # Hide the main window

# Ask user to select a folder
folder_selected = filedialog.askdirectory(title="Select a Base Folder")

if not folder_selected:
    print("No folder selected. Exiting.")
    exit()

def organize_files_by_type(base_folder):
    """
    Organize files into folders based on their file type (extension).

    Parameters:
    - base_folder (str): The path to the base folder to organize.

    Returns:
    - None
    """
    
    # Traverse all files and subfolders
    for root_folder, subdirs, files in os.walk(base_folder):
        for filename in files:
            file_path = os.path.join(root_folder, filename)
            if os.path.isfile(file_path):
                # Get the file extension and make it lowercase
                file_extension = os.path.splitext(filename)[1].lower()

                # Skip hidden/system files (like .DS_Store or .gitignore)
                if file_extension == '':
                    continue
                
                # Create a folder based on file extension
                type_folder = os.path.join(base_folder, file_extension[1:].upper() + "_FILES")  # Remove the leading '.' and capitalize
                if not os.path.exists(type_folder):
                    os.makedirs(type_folder)
                
                # Move the file to the corresponding folder
                new_file_path = os.path.join(type_folder, filename)
                
                # If a file with the same name exists, rename it
                if os.path.exists(new_file_path):
                    name, ext = os.path.splitext(filename)
                    counter = 1
                    while os.path.exists(new_file_path):
                        new_filename = f"{name}_{counter}{ext}"
                        new_file_path = os.path.join(type_folder, new_filename)
                        counter += 1
                
                shutil.move(file_path, new_file_path)
                print(f"Moved: {file_path} -> {new_file_path}")

# Organize the files in the selected folder
organize_files_by_type(folder_selected)

print("All files have been organized by file type.")
