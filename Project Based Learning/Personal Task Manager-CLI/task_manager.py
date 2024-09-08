import os

DATA_FILE = 'tasks.txt'
absolute_path = os.path.abspath(DATA_FILE)


#Read File
def read_file():
    file = open(absolute_path, "r")
    file_contents = file.read()
    file.close()
    return file_contents

#Write File
def write_file(str_to_write):
    file = open(absolute_path, "w", encoding='utf-8')
    file.write(str_to_write)
    file.close()

#Append File
def append_file(str_to_write):
    file = open(absolute_path, "a", encoding='utf-8')
    file.write(f"{str_to_write}\n")
    file.close()

#Add Task
def add_task(task_info: str):
    append_file(task_info)

#Remove Task
def remove_task(task_num: int):
    pass

#view List
def view_list():
    print(read_file())


#View Task
def view_task(task_num: int):
    pass

# Update Task
def update_task(task_num: int, task_info: str):
    pass

def main_loop():
    while True:
        print('-------------------------------------------------------------')
        print('|                   Personal Task Manager                   |')
        print('|                                                           |')
        print('|    1. Add A Task                                          |')
        print('|    2. Remove A Task                                       |')
        print('|    3. Update A Task                                       |')
        print('|    4. View A Task                                         |')
        print('|    5. View Task List                                      |')
        print('|    0. Quit                                                |')
        print('|                                                           |')
        print('-------------------------------------------------------------\n')
        print("Current Tasks:")
        with open(absolute_path, "r") as file:
            for task in file:
                print(f"\t{task}")
        file.close()
        option = int(input("Choose the option by number: "))

        if option == 0:
            break
        elif option == 1:
            task = ""
            while task == "":
                task = input("Please input the task you would like to add: ")
                if task != "":
                    break
            os.system('cls')
            add_task(task)            
        elif option == 2:
            task_num = ""
            while task_num == "":
                task_num = int(input("Please input the task you would like to remove: "))
                if task_num != "":
                    break
            os.system('cls')
            remove_task(task_num)            
        elif option == 3:
            task_num = ""
            task_text = ""
            while task_num == "":
                task_num = int(input("Please input the task you would like to update: "))
                if task_num != "":
                    break
            while task_text == "":
                task_text = int(input("What would you like to update the task to?: "))
                if task_text != "":
                    break
            os.system('cls')
            update_task(task_num, task_text)            
        elif option == 4:
            task_num = ""
            while task_num == "":
                task_num = int(input("Please input the task you would like to view: "))
                if task_num != "":
                    break
            os.system('cls')
            view_task(task_num)
        elif option == 5:
            os.system('cls')
            view_list()
    
        
        

if __name__ == '__main__':
    main_loop()
