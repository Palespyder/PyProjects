class TaskNode():
    def __init__(self, description, priority, due_date) -> None:
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.is_done = False
        self.next = None


class TaskManager():
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    # Add functions
    def prepend(self, description, priority, due_date):
        new_node = TaskNode(description, priority, due_date)
        if self.head is not None:
            temp = self.head
            self.head = new_node
            new_node.next = temp
        elif self.is_empty():
            self.head = new_node
            self.tail = new_node
            
            

    def append(self, description, priority, due_date):
        new_node = TaskNode(description, priority, due_date)
        if self.is_empty():
            self.tail = new_node
            self.head = new_node
        else:
            temp = self.tail
            self.tail = new_node
            temp.next = new_node

    def insert(self, index):
        pass

    # Delete functions
    def pop_first(self):
        if self.head is None:
            return None
        else:
            temp = self.head
            self.head = temp.next
            return temp

    def pop(self):
        if self.tail is None:
            return None
        else:
            temp = self.head
            prev = None
            while temp.next is not None:
                prev = temp
                temp = temp.next
            self.tail = prev
            prev.next = None
            return temp


    def remove_by_value(self, description):
        if self.head.description == description:
            self.pop_first()
        elif self.tail.description == description:
            self.pop()
        else:
            pass

    

    def remove_at_index(self, index):
        pass

    # Search functions

    def search(self, description):
        temp = self.head
        while temp is not None:          
                if temp.description == description:
                    return temp
                else:
                    temp = temp.next

    # Update functions
    def update_at_position(self, index, new_value):
        pass

    def update_at_value(self, old_value, new_value):
        pass

    # Utility functions
    def is_empty(self):
        if self.head is None and self.tail is None:
            return True
        else: 
            return False

    def length(self):
        count = 0
        temp = self.head
        while temp is not None:
            count += 1
            temp = temp.next
        return count

    def clear(self):
        self.head = None
        self.tail = None

    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail

    def print_list(self):
        temp = self.head
        while temp is not None:          
                print(type(temp))
                temp = temp.next




    