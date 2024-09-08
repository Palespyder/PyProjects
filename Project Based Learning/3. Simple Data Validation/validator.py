def main():
    print("Simple Data Validation Tool\n")
    
    # Initialize variables for the type of data to validate and the list to store input for validation
    validate_type = ""
    validation_list = []
    
    # Loop until a valid type ('email', 'phone', 'cc') is provided
    while validate_type == "":
        validate_type = input("What type of data would you like to validate (email, phone, cc): ")  
        
        # Code Review: This validation is verbose, could be simplified using a list of valid types. 
        # Refactor using a list to avoid repetitive conditions. 
        if validate_type != 'email' and validate_type != 'phone' and validate_type != 'cc':
            print("Invalid Type! Please try again!")
            validate_type = ""
        
        # Email validation process starts here
        elif validate_type == 'email':
            num_emails = 0
            while num_emails == 0:
                # Code Review: This could fail if the user inputs non-numeric values; add try-except block for safer input handling
                num_emails = int(input("How many emails would you like to validate?: "))
                if num_emails == 0:
                    print("You must have greater than 0 emails")
                elif num_emails > 0:
                    # Collect email inputs
                    for i in range(num_emails):
                        validation_list.append(str(input(f"Please input email #{i + 1}: ")))
                    # Validate each email in the list
                    for email in validation_list:
                        validate_email(email)
                    break
        
        # Phone validation process starts here
        elif validate_type == 'phone':
            num_phones = 0
            while num_phones == 0:
                num_phones = int(input("How many phone numbers would you like to validate?: "))
                if num_phones == 0:
                    print("You must have greater than 0 phone numbers")
                elif num_phones > 0:
                    # Collect phone inputs
                    for i in range(num_phones):
                        validation_list.append(str(input(f"Please input phone #{i + 1}: ")))
                    # Validate each phone number in the list
                    for phone in validation_list:
                        validate_phone(phone)
                    break
        
        # Credit card validation process starts here
        elif validate_type == 'cc':
            num_cc = 0
            while num_cc == 0:
                num_cc = int(input("How many credit cards would you like to validate?: "))
                if num_cc == 0:
                    print("You must have greater than 0 credit cards")
                elif num_cc > 0:
                    # Collect credit card inputs
                    for i in range(num_cc):
                        validation_list.append(str(input(f"Please input CC #{i + 1}: ")))
                    # Validate each credit card number in the list
                    for cc in validation_list:
                        validate_cc(cc)
                    break

# Validate email function
def validate_email(email: str):
    # Code Review: Use a more robust regex pattern that covers a wider range of valid email formats.
    import re
    pattern = re.compile(r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?")
  
    if not re.match(pattern, email):
        print(f"{email} is a not a valid email.")
    else:
        print(f"{email} is a valid email.")

# Validate phone number function
def validate_phone(phone: str):
    import re
    # Code Review: This regex only works with the format XXX-XXX-XXXX. Consider updating the regex to handle other formats.
    pattern = re.compile("^[\dA-Z]{3}-[\dA-Z]{3}-[\dA-Z]{4}$", re.IGNORECASE)

    if not re.match(pattern, phone):
        print(f"{phone} is a not a valid phone number.")
    else:
        print(f"{phone} is a valid phone number.")

# Validate credit card function using Luhn's Algorithm
def validate_cc(cc_num: str):
    """
    Validate the credit card number using Luhn's Algorithm.
    
    Parameters:
    cc_num (str): The credit card number entered by the user in the input box.
    
    Returns:
    None
    """
    initial_cc_num = cc_num
    # Code Review: This assumes spaces are the only delimiter. It could be enhanced to handle dashes or other separators.
    cc_num = int(cc_num.replace(' ', ''))  # Remove spaces from the input
    # Convert the card number (string) into a list of integers
    card_digits = [int(digit) for digit in str(cc_num)]
    
    # Start from the second-to-last digit and double every second digit moving left
    for i in range(len(card_digits) - 2, -1, -2):
        card_digits[i] *= 2
        # If the result of doubling is greater than 9, subtract 9 (sum the digits of the two-digit result)
        if card_digits[i] > 9:
            card_digits[i] -= 9
    
    # Calculate the total sum of all digits after the transformation
    total_sum = sum(card_digits)
    
    # If the total sum is divisible by 10, the card is valid
    if total_sum % 10 == 0:
        print(f"{initial_cc_num} is a valid CC number.")
    else:
        print(f"{initial_cc_num} is a NOT valid CC number.")

# Entry point of the program
if __name__ == '__main__':
    main()
