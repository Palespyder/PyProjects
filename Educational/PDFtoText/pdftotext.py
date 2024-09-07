import tkinter as tk
from tkinter import filedialog
from gtts import gTTS
import PyPDF2
import json
import os

# Global variables
saved_page_file = 'saved_page.json'

def load_saved_page():
    """
    Load the last saved page number from a JSON file.

    Returns:
    - int: The last saved page number, or 0 if the file does not exist or has no page number.
    """
    if os.path.exists(saved_page_file):
        with open(saved_page_file, 'r') as file:
            data = json.load(file)
            return data.get('page', 0)
    return 0

def save_page(page_number):
    """
    Save the current page number to a JSON file.

    Parameters:
    - page_number (int): The page number to save.
    """
    with open(saved_page_file, 'w') as file:
        json.dump({'page': page_number}, file)

def text_to_speech(text):
    """
    Convert text to speech and play the audio file.

    Parameters:
    - text (str): The text to convert to speech.
    """
    tts = gTTS(text=text, lang='en')
    audio_file = 'speech.mp3'
    tts.save(audio_file)
    os.system(f"start {audio_file}")  # On Windows
    # os.system(f"afplay {audio_file}")  # On macOS
    # os.system(f"mpg321 {audio_file}")  # On Linux

def read_pdf():
    """
    Read text from a selected PDF file, starting from a specified page, and convert the text to speech.
    """
    file_path = filedialog.askopenfilename(
        filetypes=[("PDF Files", "*.pdf")], title="Choose a PDF file")
    
    if not file_path:
        return

    start_page = int(start_page_entry.get() or 0)
    voice_id = voice_var.get()
    
    with open(file_path, "rb") as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        
        for page in range(start_page, len(reader.pages)):
            text += reader.pages[page].extract_text()
            save_page(page)
        
        text_to_speech(text)

# Initialize Tkinter
root = tk.Tk()
root.title("PDF to Speech Converter")
root.geometry("400x300")

# Speech speed input
speed_label = tk.Label(root, text="Speech Speed (Default 100):")
speed_label.pack(pady=10)
speed_entry = tk.Entry(root)
speed_entry.pack(pady=10)

# Voice selection dropdown
voice_label = tk.Label(root, text="Select Voice:")
voice_label.pack(pady=10)
voice_var = tk.StringVar(value="en")  # gTTS uses language codes instead of voice names
voice_dropdown = tk.OptionMenu(root, voice_var, "en")  # Default to English
voice_dropdown.pack(pady=10)

# Start page input
start_page_label = tk.Label(root, text="Start Reading from Page (Default 0):")
start_page_label.pack(pady=10)
start_page_entry = tk.Entry(root)
start_page_entry.pack(pady=10)
start_page_entry.insert(0, str(load_saved_page()))

# Button to select PDF and read
select_button = tk.Button(root, text="Select PDF and Read", command=read_pdf)
select_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
