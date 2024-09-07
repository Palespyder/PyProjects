from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *

# Create the main window
root = tb.Window(themename="superhero")
root.title("Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Global variable for storing the equation
equation = StringVar()

# Function to update the equation in the text entry
def press(num):
    current_equation = equation.get()
    equation.set(current_equation + str(num))

# Function to evaluate the final expression
def equalpress():
    try:
        result = str(eval(equation.get()))  # Evaluate the equation
        equation.set(result)
    except Exception as e:
        equation.set("Error")

# Function to clear the input
def clear():
    equation.set("")

# Create the display entry box
entry_box = tb.Entry(root, textvariable=equation, font=("Helvetica", 18), justify="right", bootstyle="info")
entry_box.grid(row=0, column=0, columnspan=4, ipadx=10, ipady=10, padx=10, pady=10)

# Create number buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:
    if text == '=':
        button = tb.Button(root, text=text, width=5, bootstyle="success", command=equalpress)
    else:
        button = tb.Button(root, text=text, width=5, bootstyle="secondary", command=lambda t=text: press(t))
    button.grid(row=row, column=col, padx=5, pady=5)

# Create clear button
clear_button = tb.Button(root, text="Clear", width=5, bootstyle="danger", command=clear)
clear_button.grid(row=5, column=0, columnspan=4, padx=5, pady=10, sticky="nsew")

# Start the application
root.mainloop()
