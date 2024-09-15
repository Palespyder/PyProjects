class Node():
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree():
    def __init__(self) -> None:
        self.root = None

   
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while temp is not None:
            if new_node.value == temp.value:
                return False
            elif new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
            elif new_node.value > temp.value:
                if temp.right is None:
                    temp.right = new_node
                    return True
            else:
                return False
        return False
        



        

    def contains(self, value):
        if self.root is None:
            return False
        elif self.root.value == value:
            return True
        temp = self.root
        while temp is not None:
            if value == temp.value:
                return True
            elif value < temp.value:
                temp = temp.left                
            elif value > temp.value:
                temp = temp.right                
            else:
                return False  # Prevent infinite loop
        return False




my_tree = BinarySearchTree()

my_tree.insert(75)

my_tree.insert(15)



