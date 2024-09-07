import zipfile
import base64
import os

def compress_and_encode(folder_path, output_file):
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
        folder_path = filedialog.askdirectory(title="Select Folder to Compress")
        if folder_path:
            output_file = filedialog.asksaveasfilename(defaultextension=".b64", filetypes=[("Base64 Encoded Files", "*.b64")], title="Save Encoded File As")
            if output_file:
                compress_and_encode(folder_path, output_file)
                tk.messagebox.showinfo("Success", f"Files compressed and encoded successfully:\n{output_file}")

    root = tk.Tk()
    root.title("Folder Compressor and Encoder")
    root.geometry("300x150")

    select_button = tk.Button(root, text="Select Folder and Encode", command=select_folder_and_save)
    select_button.pack(pady=50)

    root.mainloop()
