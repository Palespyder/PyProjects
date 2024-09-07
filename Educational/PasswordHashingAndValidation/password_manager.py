import hashlib
import getpass

def hash_password(password: str) -> str:
    """
    Hashes a password using SHA-256.

    This function takes a plain-text password, encodes it to bytes, and then computes its SHA-256 hash. 
    The resulting hash is returned as a hexadecimal string.

    Args:
        password (str): The plain-text password to be hashed.

    Returns:
        str: The hexadecimal representation of the SHA-256 hash of the password.
    """
    # Create a new sha256 hash object
    hasher = hashlib.sha256()
    # Update the hash object with the bytes of the password
    hasher.update(password.encode('utf-8'))
    # Return the hexadecimal representation of the hash
    return hasher.hexdigest()

def validate_password(stored_hash: str, password: str) -> bool:
    """
    Validates a password by comparing its hash with the stored hash.

    This function hashes the provided password and compares it with the stored hash. 
    It returns True if the hashes match, indicating the password is correct, and False otherwise.

    Args:
        stored_hash (str): The stored hash of the password to be validated.
        password (str): The plain-text password to be validated.

    Returns:
        bool: True if the provided password matches the stored hash, False otherwise.
    """
    # Hash the provided password
    provided_hash = hash_password(password)
    # Return whether the provided hash matches the stored hash
    return provided_hash == stored_hash

def main():
    """
    Main function to provide a command-line interface for hashing and validating passwords.

    This function repeatedly presents a menu to the user with options to:
    1. Hash a new password.
    2. Validate a password against a stored hash.
    3. Exit the application.

    Depending on the user's choice, it either hashes a new password, validates an existing password, or exits the application.
    """
    while True:
        # Display the menu options
        print("Password Manager")
        print("1. Hash a new password")
        print("2. Validate a password")
        print("3. Exit")

        # Get the user's choice
        choice = input("Enter your choice: ")

        if choice == '1':
            # Hash a new password
            password = getpass.getpass("Enter a new password: ")
            hashed = hash_password(password)
            print(f"Hashed password: {hashed}")
            # In a real application, you would save the hashed password to a file or database

        elif choice == '2':
            # Validate a password
            stored_hash = input("Enter the stored hash: ")
            password = getpass.getpass("Enter the password to validate: ")
            if validate_password(stored_hash, password):
                print("Password is valid.")
            else:
                print("Invalid password.")

        elif choice == '3':
            # Exit the application
            print("Exiting...")
            break

        else:
            # Handle invalid choices
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
