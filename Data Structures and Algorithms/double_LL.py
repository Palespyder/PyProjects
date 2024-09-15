class Node():
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.prev = None



class DoubleLinkedList():
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

    def append(self, value):
        new_node = Node(value)
        temp = self.tail
        new_node.prev = temp
        temp.next = new_node
        self.tail = new_node
        new_node.next = None

    def pop(self):
        temp = self.tail
        self.tail = temp.prev
        self.tail.next = None
        return temp
    
    def prepend(self, value):
        new_node = Node(value)        
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def pop_first(self):
        temp = self.head
        self.head = self.head.next
        self.head.prev = None
        return temp
    
    def get_by_value(self, value):
        temp = self.head
        while temp is not None:
            if temp.value == value:
                return temp
            else:
                temp = temp.next
        return None
    
    def get_by_index(self, index):
        if index < 0 or index >= self.get_length():
            return None
        temp = self.head
        count = 0
        for _ in range(index):
            temp = temp.next
        if temp is not None:
            return temp
        else:
            return None
        
    def set_by_value(self, value, new_value):
        temp = self.head
        while temp is not None:
            if temp.value == value:
                temp.value = new_value
                return True
            else:
                temp = temp.next
        return False

    def set_by_index(self, index, new_value):
        if index < 0 or index >= self.get_length():
            return False
        temp = self.head
        count = 0
        for _ in range(index):
            temp = temp.next
        if temp is not None:
            temp.value = new_value
            return True
        else:
            return False
        
    def insert(self, index, value):
        if index < 0 or index >= self.get_length():
            return False
        temp = self.head
        count = 0
        for _ in range(index - 1):
            temp = temp.next
        if temp is not None:
            new_node = Node(value)
            next = temp.next            
            temp.next = new_node
            new_node.prev = temp
            new_node.next = next
            return True
        else:
            return False
        
    def remove(self, index):
        if index < 0 or index >= self.get_length():
            return False
        temp = self.head
        count = 0
        for _ in range(index):
            temp = temp.next
        if temp is not None:
            next = temp.next
            prev = temp.prev
            temp.next.prev = prev
            temp.prev.next = next            
            return True
        else:
            return False

    def get_length(self):
        count = 0
        temp = self.head
        while temp is not None:
            count += 1
            temp = temp.next
        return count
    
    def print_ll(self):
        temp = self.head
        while temp is not None:
            print(f"Value: {temp.value} - Previous: {temp.prev} - Next: {temp.next}")
            temp = temp.next




my_linkedlist = DoubleLinkedList(4)
my_linkedlist.append(7)
my_linkedlist.append(12)
my_linkedlist.prepend(18)
my_linkedlist.prepend(1775)

if my_linkedlist.insert(1, 999):
    my_linkedlist.print_ll()

if my_linkedlist.remove(1):
    my_linkedlist.print_ll()



