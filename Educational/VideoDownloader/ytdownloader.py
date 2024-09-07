import tkinter as tk
from tkinter import messagebox, filedialog
from pytube import YouTube

# Function to handle downloading the video
def download_video():
    url = url_entry.get()  # Get the URL from the input field

    # Check if the URL field is empty
    if not url:
        messagebox.showerror("Error", "Please enter a valid YouTube URL")
        return

    try:
        # Create a YouTube object using the URL
        yt = YouTube(url)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch video. Please check the URL.\nError: {e}")
        return

    # Get the selected format and quality from the radio buttons
    selected_quality = quality_var.get()
    selected_format = format_var.get()

    # Filter the streams based on the user's selection
    if selected_format == "Video":
        if selected_quality == "Highest":
            stream = yt.streams.get_highest_resolution()  # Get the highest resolution video stream
        else:
            stream = yt.streams.filter(progressive=True, file_extension='mp4').get_by_resolution(selected_quality)
    elif selected_format == "Audio":
        stream = yt.streams.filter(only_audio=True).first()  # Get the first available audio stream

    # If no stream is found, show an error message
    if not stream:
        messagebox.showerror("Error", "Selected quality or format not available.")
        return

    # Ask the user where to save the video
    folder = filedialog.askdirectory()  # Open file dialog to choose folder
    if not folder:
        return  # If no folder selected, return without downloading

    # Download the selected stream to the chosen folder
    try:
        messagebox.showinfo("Downloading", "Downloading started...")
        stream.download(output_path=folder)  # Download the video/audio stream
        messagebox.showinfo("Success", f"Download completed and saved to {folder}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download video. Error: {e}")

# Set up the main GUI window using tkinter
app = tk.Tk()
app.title("YouTube Video Downloader")  # Set the window title
app.geometry("500x400")  # Set the window size

# URL Input Field and Label
url_label = tk.Label(app, text="Enter YouTube URL:")  # Label for the URL input
url_label.pack(pady=10)  # Padding for spacing

url_entry = tk.Entry(app, width=50)  # Input field for the URL
url_entry.pack(pady=5)

# Format Selection (Video or Audio)
format_var = tk.StringVar(value="Video")  # Variable to store selected format
format_label = tk.Label(app, text="Select Format:")  # Label for format selection
format_label.pack(pady=5)

format_video = tk.Radiobutton(app, text="Video", variable=format_var, value="Video")  # Radio button for "Video"
format_video.pack()

format_audio = tk.Radiobutton(app, text="Audio", variable=format_var, value="Audio")  # Radio button for "Audio"
format_audio.pack()

# Quality Selection for Video
quality_var = tk.StringVar(value="Highest")  # Variable to store selected video quality
quality_label = tk.Label(app, text="Select Quality (Video only):")  # Label for video quality selection
quality_label.pack(pady=5)

quality_high = tk.Radiobutton(app, text="Highest", variable=quality_var, value="Highest")  # Radio button for "Highest" quality
quality_high.pack()

quality_720p = tk.Radiobutton(app, text="720p", variable=quality_var, value="720p")  # Radio button for "720p"
quality_720p.pack()

quality_480p = tk.Radiobutton(app, text="480p", variable=quality_var, value="480p")  # Radio button for "480p"
quality_480p.pack()

# Download Button to trigger the download
download_button = tk.Button(app, text="Download", command=download_video)
download_button.pack(pady=20)  # Padding for spacing

# Start the Tkinter event loop to display the window
app.mainloop()
