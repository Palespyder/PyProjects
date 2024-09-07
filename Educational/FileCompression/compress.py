import zipfile
import base64
import os

def compress_and_encode(folder_path, output_file):
    """
    Compresses a folder into a ZIP file and encodes the ZIP file into Base64 format.

    Parameters:
    - folder_path (str): The path to the folder to be compressed.
    - output_file (str): The path to the output file where the Base64 encoded data will be saved.
    
    Process:
    1. Creates a temporary ZIP file.
    2. Compresses the entire folder into the ZIP file.
    3. Reads the ZIP file and encodes its contents into Base64.
    4. Saves the Base64 encoded data to the specified output file.
    5. Removes the temporary ZIP file after encoding.

    Returns:
    None
    """
    # Create a temporary ZIP file
    zip_file = 'temp.zip'
    
    # Compress the folder into the ZIP file
    with zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, folder_path))
    
    # Encode the ZIP file in Base64
    with open(zip_file, 'rb') as file:
        encoded_string = base64.b64encode(file.read())
    
    # Write the Base64 encoded string to the output file
    with open(output_file, 'wb') as file:
        file.write(encoded_string)
    
    # Clean up temporary ZIP file
    os.remove(zip_file)

if __name__ == "__main__":
    import tkinter as tk
    from tkinter import filedialog

    def select_folder_and_save():
        """
        Opens file dialogs for selecting a folder to compress and a file to save the encoded data.
        Calls the `compress_and_encode` function with the selected paths.
        
        Returns:
        None
        """
        # Open a dialog to select the folder to compress
        folder_path = filedialog.askdirectory(title="Select Folder to Compress")
        if folder_path:
            # Open a dialog to select where to save the Base64 encoded file
            output_file = filedialog.asksaveasfilename(
                defaultextension=".b64", 
                filetypes=[("Base64 Encoded Files", "*.b64")],
                title="Save Encoded File As"
            )
            if output_file:
                # Compress and encode the selected folder, and save the result
                compress_and_encode(folder_path, output_file)
                tk.messagebox.showinfo("Success", f"Files compressed and encoded successfully:\n{output_file}")

    # Create and configure the Tkinter window
    root = tk.Tk()
    root.title("Folder Compressor and Encoder")
    root.geometry("300x150")

    # Create and place the "Select Folder and Encode" button
    select_button = tk.Button(root, text="Select Folder and Encode", command=select_folder_and_save)
    select_button.pack(pady=50)

    # Start the Tkinter event loop
    root.mainloop()
