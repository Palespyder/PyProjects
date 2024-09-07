from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb
from ttkbootstrap import ttk
from PIL import Image, ImageTk  # To handle png images

# Create the main window
root = tb.Window(themename="superhero")
frame = tb.Frame(root, padding=5)
frame.pack(fill=BOTH, expand=YES)
root.title("Temperature Conversion App")
root.iconbitmap(True, 'img/temp.png')
root.geometry('500x350')


def ConvertTemp(type: str, temp: float) -> list[float]:
    """
    Convert temperature between Celsius, Fahrenheit, and Kelvin.

    Parameters:
    - type (str): The type of the input temperature ('f' for Fahrenheit, 'c' for Celsius, 'k' for Kelvin).
    - temp (float): The temperature value to convert.

    Returns:
    - list[float]: A list containing temperatures in Fahrenheit, Celsius, and Kelvin.
    """
    if type == "f":
        celsius = float((temp - 32.0) * 5/9)
        kelvin = float((temp - 32.0) * (5/9) + 273.15)
        result = [temp, celsius, kelvin]
    elif type == 'c':
        fahrenheit = float((temp * 9/5) + 32.0)
        kelvin = float(temp + 273.15)
        result = [fahrenheit, temp, kelvin]
    elif type == 'k':
        fahrenheit = float((temp - 273.15) * 9/5 + 32)
        celsius = float(temp - 273.15)
        result = [fahrenheit, celsius, temp]
    else:
        return [0, 0, 0]
    return result


# Create a label
titlebar = tb.Label(frame, text="Temperature Converter", font=("Helvetica", 28), bootstyle="primary")
titlebar.pack(pady=50)

# Create an input label and textbox
tb.Label(frame, text="Enter a Temperature").pack()

# Create a frame to hold the entry and combobox and center it
temp_frame = tb.Frame(frame)
temp_frame.pack(pady=10, expand=True)

# Entry widget for temperature input
tempEntry = tb.Entry(temp_frame)
tempEntry.pack(side=LEFT, padx=5, pady=5)

# Combobox for selecting temperature units
unit_options = ["Celsius", "Fahrenheit", "Kelvin"]
unit_combobox = ttk.Combobox(temp_frame, values=unit_options, state="readonly")
unit_combobox.current(0)  # Set Celsius as the default selection
unit_combobox.pack(side=LEFT, padx=5, pady=5)

# Load the images for Celsius, Fahrenheit, and Kelvin
celcius_img = ImageTk.PhotoImage(Image.open("img/celcius.png").resize((30, 30)))
farenheit_img = ImageTk.PhotoImage(Image.open("img/farenheit.png").resize((30, 30)))
kelvin_img = ImageTk.PhotoImage(Image.open("img/kelvin.png").resize((30, 30)))

def on_convert():
    """
    Handle the conversion of temperature and update the result display.
    """
    temp = float(tempEntry.get())
    unit = unit_combobox.get().lower()[0]  # Get the first letter of the selected unit
    results = ConvertTemp(unit, temp)

    # Clear previous results before displaying new ones
    for widget in result_frame.winfo_children():
        widget.destroy()

    # Display Fahrenheit result
    farenheit_frame = tb.Frame(result_frame)
    farenheit_frame.pack(pady=5)
    farenheit_icon = tb.Label(farenheit_frame, image=farenheit_img)
    farenheit_icon.pack(side=LEFT)
    farenheit_label = tb.Label(farenheit_frame, text=f"{results[0]:.2f}°", font=("Helvetica", 16))
    farenheit_label.pack(side=LEFT, padx=10)

    # Display Celsius result
    celsius_frame = tb.Frame(result_frame)
    celsius_frame.pack(pady=5)
    celsius_icon = tb.Label(celsius_frame, image=celcius_img)
    celsius_icon.pack(side=LEFT)
    celsius_label = tb.Label(celsius_frame, text=f"{results[1]:.2f}°", font=("Helvetica", 16))
    celsius_label.pack(side=LEFT, padx=10)

    # Display Kelvin result
    kelvin_frame = tb.Frame(result_frame)
    kelvin_frame.pack(pady=5)
    kelvin_icon = tb.Label(kelvin_frame, image=kelvin_img)
    kelvin_icon.pack(side=LEFT)
    kelvin_label = tb.Label(kelvin_frame, text=f"{results[2]:.2f}K", font=("Helvetica", 16))
    kelvin_label.pack(side=LEFT, padx=10)

# Create a Button for conversion
convert_button = tb.Button(frame, text="Convert", bootstyle="success", command=on_convert)
convert_button.pack(pady=20)

# Create a frame to hold the result icons and labels
result_frame = tb.Frame(frame)
result_frame.pack(pady=10)

root.mainloop()
