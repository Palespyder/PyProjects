# Folder Compressor and Encoder

This Python application allows you to select a folder, compress its contents into a ZIP file, encode the ZIP file into Base64, and save it as a file. It provides a simple graphical user interface (GUI) using Tkinter to facilitate the process.

## Features

- Compresses a selected folder into a ZIP file.
- Encodes the ZIP file into Base64 format.
- Saves the Base64 encoded file to a specified location.
- User-friendly interface with folder selection and file save dialogs.

## Dependencies

- `tkinter` (for GUI)
- Python's built-in `zipfile`, `base64`, and `os` modules

## How It Works

1. **Folder Compression**: The selected folder is compressed into a ZIP file using Python's `zipfile` module.
2. **Base64 Encoding**: The ZIP file is encoded in Base64 format using Python's `base64` module.
3. **File Saving**: The Base64 encoded content is saved to the specified output file.

## Code Overview

- **compress_and_encode(folder_path, output_file)**:
  - **Parameters**:
    - `folder_path` (str): Path to the folder to be compressed.
    - `output_file` (str): Path to the output file where the Base64 encoded data will be saved.
  - **Functionality**:
    - Compresses the folder into a temporary ZIP file.
    - Encodes the ZIP file into Base64.
    - Writes the encoded content to the output file.
    - Cleans up by removing the temporary ZIP file.

- **Tkinter GUI**:
  - A simple Tkinter window allows users to select a folder and save the Base64 encoded file.
  - Uses `filedialog` to open folder selection and file save dialogs.

## Running the Application

1. Save the provided code to a file, for example, `compress_and_encode.py`.
2. Ensure you have Python installed on your system.
3. Run the file using Python:

    ```sh
    python compress_and_encode.py
    ```

4. The Tkinter window will appear. Click the "Select Folder and Encode" button to select the folder you want to compress and encode.
5. Choose where to save the Base64 encoded file when prompted.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Python's `tkinter` for providing a simple and effective GUI toolkit.
- Python's built-in `zipfile`, `base64`, and `os` modules for handling file compression, encoding, and file operations.

Feel free to enhance the application or customize it as needed. Enjoy using your folder compressor and encoder!
