class Item():
    def __init__(self, value) -> None:
        self.value = value
        self.next = None



class Stack():
    def __init__(self, value) -> None:
        new_item = Item(value)
        self.head = new_item

    def push(self, value):
        new_item = Item(value)        
        new_item.next = self.head
        self.head = new_item
        

    def pop(self):
        temp = self.head
        self.head = temp.next
        return temp
    
    def print_stack(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


#my_stack = Stack(1)
#my_stack.push(25)
#my_stack.push(35)

#my_stack.push(22)
#my_stack.push(77)
#my_stack.pop()


#my_stack.print_stack()

#Queue is very similar but instead of popping off the head, you would pop off the tail.

class Item():
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.prev = None



class Queue():
    def __init__(self, value) -> None:
        new_item = Item(value)
        self.head = new_item
        self.tail = new_item

    def enqueue(self, value):
        new_item = Item(value)        
        new_item.next = self.head
        new_item.prev = None
        self.head.prev = new_item
        self.head = new_item
        

    def dequeue(self):
        temp = self.tail
        self.tail = temp.prev
        self.tail.next = None
        return temp
    
    def print_queue(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


my_queue = Queue(2)

my_queue.enqueue(6)

my_queue.print_queue()

print(my_queue.dequeue().value)
my_queue.print_queue()