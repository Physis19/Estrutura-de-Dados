class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self._size = 0
    
    def append(self, data):
        if self.head == None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            current = self.head
            while(current.next):
                current = current.next
            current.next = new_node
            new_node.previous = current
            new_node.next = None
    
    def prepend(self, data):
        if self.head == None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.previous = new_node
            new_node.next = self.head
            self.head = new_node
    
    def print_list(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next

lista = DoublyLinkedList()
lista.append(1)
lista.append(2)
lista.append(3)
lista.append(4)
lista.prepend(10)
lista.print_list()


