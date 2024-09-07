# PDF to Speech Converter

This Python application converts the text from a selected PDF file to speech. It uses `gTTS` (Google Text-to-Speech) for text-to-speech conversion and `PyPDF2` for reading text from PDF files. The application allows users to start reading from a specific page and remembers the last read page using a JSON file.

## Features

- Convert PDF text to speech.
- Start reading from a specified page.
- Save and load the last read page.
- Basic GUI for user interaction using Tkinter.

## Requirements

- Python 3.x
- `gTTS`: Google Text-to-Speech library
- `PyPDF2`: Library for reading PDF files
- `Pillow`: Required for image handling (usually installed with `Pillow`)

You can install the required libraries using pip:

```bash
pip install gtts PyPDF2 Pillow
