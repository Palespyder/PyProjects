class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None    

        
class LinkedList:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def append(self, value) -> bool:
        # Create new node
        # add node to the end
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node        
        self.length += 1 
        return True
    
    def pop(self) -> Node:
        if self.tail == None:
            return None
        elif self.tail == self.head:
            temp = self.head
            self.head = None
            self.tail = None
            return temp
        else:
            temp = self.head
            pre = self.head
            while temp.next is not None:
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
            self.length -= 1
            return temp

    def prepend(self, value):
        # create new node
        # add node to the beginning
        new_node = Node(value)
        new_node.next = self.head.next
        self.head = new_node        
        self.length += 1

    def pop_first(self):
        if self.head == None:
            return None
        elif self.head == self.tail:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return temp
        else:
            temp = self.head
            self.head = temp.next
            self.length -= 1
            return temp
        
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for i in range(index):
            temp = temp.next
        return temp
    
    def set(self, index, value):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for i in range(index):
            temp = temp.next
        temp.value = value


    def insert(self, index, value) -> bool:
        # create new node
        # insert node at index.
        if index < 0 or index >= self.length:
            return False
        new_node = Node(value)
        temp = self.head
        for i in range(index - 1):
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            self.pop_first()
        elif index == self.length - 1:
            self.pop()
        else:
            prev = self.get(index - 1)
            temp = prev.next
            prev.next = temp.next
            self.length -= 1            
            return temp                 
        

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        
        

        


        



 
my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(26)


my_linked_list.print_list()
print('\n\n')
my_linked_list.reverse()

my_linked_list.print_list()








                                                                                                                    