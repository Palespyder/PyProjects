import os
import re

# Define the data file path
DATA_FILE = 'tasks.txt'
absolute_path = os.path.abspath(DATA_FILE)


# Function to read the entire file
def read_file():
    """Reads the entire contents of the file."""
    with open(absolute_path, "r") as file:
        return file.read()


# Function to write to the file (overwrites existing content)
def write_file(str_to_write):
    """Overwrites the file with the provided content."""
    with open(absolute_path, "w", encoding='utf-8') as file:
        file.write(str_to_write)


# Function to append to the file
def append_file(str_to_write):
    """Appends the provided string to the file, adding a new line."""
    with open(absolute_path, "a", encoding='utf-8') as file:
        file.write(f"{str_to_write}\n")


# Function to renumber tasks in the file
def renumber_tasks():
    """Renumbers the tasks in the file, starting from 1, after removing any existing numbers."""
    with open(absolute_path, "r") as file:
        content = file.readlines()

    renumbered_content = []
    for i, line in enumerate(content):
        # Strip any existing leading numbers using regex
        cleaned_line = re.sub(r'^\d+\.\s*', '', line.strip())  # Removes existing numbers at the start
        renumbered_content.append(f"{i + 1}. {cleaned_line}\n")

    write_file(''.join(renumbered_content))


# Function to add a task to the file
def add_task(task_info: str):
    """Adds a new task and renumbers the tasks."""
    append_file(task_info)
    renumber_tasks()


# Function to remove a task by its number
def remove_task(task_num: int):
    """Removes the task at the specified task number and renumbers the tasks."""
    with open(absolute_path, 'r') as file:
        content = file.readlines()

    # Remove the line at the specified index
    if 0 <= task_num - 1 < len(content):
        del content[task_num - 1]

    write_file(''.join(content))
    renumber_tasks()


# Function to view the entire task list
def view_list():
    """Prints the entire list of tasks."""
    print(read_file())


# Function to view a specific task by its number
def view_task(task_num: int):
    """Prints the task at the specified task number."""
    with open(absolute_path, 'r') as file:
        content = file.readlines()

    if 0 <= task_num - 1 < len(content):
        print(content[task_num - 1])


# Function to update a task by its number
def update_task(task_num: int, task_info: str):
    """Updates the task at the specified task number with new information."""
    with open(absolute_path, 'r') as file:
        content = file.readlines()

    if 0 <= task_num - 1 < len(content):
        # Replace the task info and ensure it ends with a newline
        content[task_num - 1] = f"{task_info}\n"

    write_file(''.join(content))
    renumber_tasks()


# Main loop for the task manager menu
def main_loop():
    """Main loop for the task manager's user interface."""
    while True:
        # Display menu
        print('-------------------------------------------------------------')
        print('|                   Personal Task Manager                   |')
        print('|                                                           |')
        print('|    1. Add A Task                                          |')
        print('|    2. Remove A Task                                       |')
        print('|    3. Update A Task                                       |')
        print('|    4. View A Task                                         |')
        print('|    5. View Task List                                      |')
        print('|    0. Quit                                                |')
        print('-------------------------------------------------------------\n')
        print("Current Tasks:")
        with open(absolute_path, "r") as file:
            for task in file:
                print(f"\t{task.strip()}")

        option = int(input("Choose the option by number: "))

        if option == 0:
            break
        elif option == 1:
            task = input("Please input the task you would like to add: ").strip()
            if task:
                add_task(task)
        elif option == 2:
            task_num = int(input("Please input the task number you would like to remove: "))
            remove_task(task_num)
        elif option == 3:
            task_num = int(input("Please input the task number you would like to update: "))
            task_text = input("What would you like to update the task to?: ").strip()
            if task_text:
                update_task(task_num, task_text)
        elif option == 4:
            task_num = int(input("Please input the task number you would like to view: "))
            view_task(task_num)
        elif option == 5:
            view_list()


# Entry point of the program
if __name__ == '__main__':
    main_loop()
