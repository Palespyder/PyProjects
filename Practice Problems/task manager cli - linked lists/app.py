from ll import TaskManager


def main():
    task_list = TaskManager()    
    task_list.prepend("This is a description", "High", "9-15-2024")
    task_list.append("Another new one", "Low", "11/26/2024")
    task_list.append("Yet Another new one", "Low", "11/26/2024")
    task_list.prepend("This is a New first description", "High", "9-17-2024")
    task_list.prepend("First description", "High", "9-17-2024")
    task_list.append("Last Description", "Low", "11/26/2024")
    task_list.append("Test", "Low", "11/26/2024")

    task_list.print_list()
    print('\n')

    print(task_list.remove_by_value("First description"))

    print('\n')
    task_list.print_list()
    















if __name__ == '__main__':
    main()