"""Command-Line Calculator

The objective of this application is to create a calculator application using only the command line.

The key skills this will work on are Variables, Data Types, Conditionals, Loops, and Functions
"""

def calculate_total(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '/':
        return num1 / num2
    elif operator == '*':
        return num1 * num2
    elif operator == '^':
        return num1 ** num2
    else:
        return

def main():
    print("Welcome to the Command-Line Calculator\n")
    first_num = 0
    second_num = 0
    operators = ["+", "-", "/", "*", "^"]
    operator = ""
    while True:
        first_num = input("First Number: ")
    
        try:
            # Try to convert input to an integer
            first_num = int(first_num)
            break  # Exit the loop if successful
        except ValueError:
            try:
                # Try to convert input to a float if it's not an integer
                first_num = float(first_num)
                break  # Exit the loop if successful
            except ValueError:
                # If neither int nor float, prompt again
                print("Your input must be a number.\n")
    
    while True:
        second_num = input("Second Number: ")
    
        try:
            # Try to convert input to an integer
            second_num = int(second_num)
            break  # Exit the loop if successful
        except ValueError:
            try:
                # Try to convert input to a float if it's not an integer
                second_num = float(second_num)
                break  # Exit the loop if successful
            except ValueError:
                # If neither int nor float, prompt again
                print("Your input must be a number.\n")

    while operator not in operators:
        operator = input("Operator (+, -. *, /, ^): ")
        # Try to convert input to an integer
        if operator in operators:
            print(calculate_total(first_num, second_num, operator))
            break  # Exit the loop if successful
        



if __name__ == "__main__":
    main()