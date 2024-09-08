import ttkbootstrap as ttk  # Import the ttkbootstrap library for modern themed widgets.
from ttkbootstrap.constants import *  # Import constants like bootstyle for styling purposes.

def update_label(is_valid):
    """
    Update the label text to indicate if the credit card is valid or not.
    
    Parameters:
    is_valid (str): The text that should be displayed on the label.
    """
    # Update the label widget with the provided text indicating validity
    label.config(text=is_valid)

def validateCC(cc_num):
    """
    Validate the credit card number using Luhn's Algorithm.
    
    Parameters:
    cc_num (str): The credit card number entered by the user in the input box.
    
    Returns:
    None
    """
    # Convert the card number (string) into a list of integers
    card_digits = [int(digit) for digit in str(cc_num)]
    
    # Start from the second-to-last digit (moving left) and double every second digit.
    for i in range(len(card_digits) - 2, -1, -2):
        card_digits[i] *= 2
        # If the result of doubling is greater than 9, subtract 9 (i.e., sum the digits of the two-digit result)
        if card_digits[i] > 9:
            card_digits[i] -= 9
    
    # Calculate the total sum of all the digits after the transformation
    total_sum = sum(card_digits)
    
    # Check if the total sum is divisible by 10 (valid if it is)
    if total_sum % 10 == 0:
        update_label("CC is Valid!")  # Update the label to show the card is valid
    else:
        update_label("CC is Not Valid!")  # Update the label to show the card is invalid

# Create the main application window using ttkbootstrap
root = ttk.Window(themename="darkly")  # Create a window with the 'darkly' theme
root.title("Text Update Interface")  # Set the title of the window
root.geometry("300x200")  # Set the size of the window to 300x200 pixels

# Create an input box where the user will enter the credit card number
input_box = ttk.Entry(root, width=30)  # Create an entry widget with a width of 30 characters
input_box.pack(pady=20)  # Add padding around the input box

# Create a button that will validate the credit card number when clicked
button = ttk.Button(root, text="Validate Card", command=lambda: validateCC(input_box.get()))
# The button's 'command' uses a lambda function to call validateCC with the input box value
button.pack(pady=10)  # Add padding around the button

# Create a label that will display whether the card is valid or not
label = ttk.Label(root, text="", bootstyle=INFO)  # The label starts empty, styled with 'INFO' bootstyle
label.pack(pady=30)  # Add padding around the label

# Start the main event loop for the application (keeps the window open and responsive)
root.mainloop()
