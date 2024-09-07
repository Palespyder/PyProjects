# Import required modules
import tkinter as tk  # Tkinter for creating the GUI window
from tkinter import messagebox, filedialog  # Message box for error messages, filedialog for saving files
import qrcode  # QRCode generation module
from PIL import Image, ImageTk  # PIL for handling images in Tkinter
import os  # OS module to handle file operations

# Function to generate a QR code based on user input
def generate_qr_code():
    # Get the data inputted by the user from the input field
    data = input_field.get()

    # Check if the input field is empty
    if data.strip() == "":
        # If empty, show an error message and exit the function
        messagebox.showerror("Error", "Please enter some data.")
        return
    
    # Create a QRCode object with specific configuration
    qr = qrcode.QRCode(
        version=1,  # Version 1, which is a 21x21 grid
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Allows up to 7% error correction
        box_size=10,  # Size of the QR code's boxes (pixels per box)
        border=4  # Border width around the QR code
    )
    
    # Add the user data to the QR code object
    qr.add_data(data)
    
    # Make the QR code fit within the set version grid size
    qr.make(fit=True)
    
    # Create the image for the QR code with specific colors
    img = qr.make_image(fill="black", back_color="white")
    
    # Save the QR code image to a file
    qr_code_path = "qr_code.png"
    img.save(qr_code_path)
    
    # Load the saved QR code image using PIL
    img_tk = Image.open(qr_code_path)
    img_tk = ImageTk.PhotoImage(img_tk)  # Convert image to format compatible with Tkinter

    # Display the QR code in the label on the Tkinter window
    qr_label.config(image=img_tk)
    qr_label.image = img_tk  # Save reference to prevent the image from being garbage collected

    # Show the download button for saving the QR code image
    download_button.pack()

# Function to download the generated QR code to the user's chosen file location
def download_qr_code():
    # Open a file dialog to ask the user where to save the file
    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",  # Default file extension is PNG
        filetypes=[("PNG files", "*.png")]  # Allow only PNG file types
    )
    
    # If the user selects a file path, rename the temporary file to the chosen file path
    if file_path:
        os.rename("qr_code.png", file_path)  # Move the file to the selected location
        messagebox.showinfo("Success", f"QR code saved as {file_path}")  # Show a success message

# Set up the main window using Tkinter
root = tk.Tk()
root.title("QR Code Generator")  # Title for the window

# Label asking the user to input data
input_label = tk.Label(root, text="Enter data to generate QR code:")
input_label.pack(pady=10)  # Add some padding

# Input field for the user to type data
input_field = tk.Entry(root, width=40)  # Width of the input field
input_field.pack(pady=5)

# Button that calls the generate_qr_code function when clicked
generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr_code)
generate_button.pack(pady=10)

# Label where the generated QR code image will be displayed
qr_label = tk.Label(root)
qr_label.pack(pady=10)

# Download button (hidden until a QR code is generated) to save the QR code
download_button = tk.Button(root, text="Download QR Code", command=download_qr_code)

# Start the Tkinter event loop (keeps the window running)
root.mainloop()
