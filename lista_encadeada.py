class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0
    
    def _getnode(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError
        return pointer

    def append(self, elem):
        if self.head:
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(elem) 
            self._size += 1   
            
        else:
            self.head  = Node(elem) 
            self._size += 1  
    
    def __getitem__(self, index):
        pointer = self._getnode(index)
        if pointer:
            return pointer.data
        else:
            raise IndexError
    
    def __setitem__(self, index, elem):
        pointer = self._getnode(index)
        if pointer:
            pointer.data = elem
        else:
            raise IndexError
        
    def __len__(self):
        return self._size

    def index(self,  elem):
        pointer = self.head
        i = 0
        while(pointer.next):
            if pointer.data == elem:
                return i
            pointer = pointer.next
            i += 1
        raise ValueError(f'{elem} is not in list')
    
    def insert(self, index, elem):
        node = Node(elem)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            pointer = self._getnode(index - 1)
            node = Node(elem)
            node.next = pointer.next
            pointer.next = node
        self._size += 1
    
    def remove(self, elem):
        if self.head == None:
            raise ValueError
        elif self.head.data == elem:
            self.head = self.head.next
        else:
            ancestor = self.head
            pointer = self.head.next
            while(pointer):
                if pointer.data == elem:
                    ancestor.next = pointer.next
                    pointer.next = None
                ancestor = pointer
                pointer = pointer.next
        
        def __repr__(self):
            r = ""
            pointer = self.head
            while(pointer):
                r = r + str(pointer.data) + "-->"
                pointer = pointer.next
            return r
        
        def __str__(self):
            return self.__repr__()


        
lista = LinkedList()
node1 = lista.append(1)
node2 = lista.append(2)
node3 = lista.append(3)
lista.append(22)
print(len(lista))
print('---------------------------')
print(lista[0])
print(lista[1])
print(lista[2])
print('---------------------------')
lista.remove(1)
print('---------------------------')
print(lista[0])
print(lista[1])
print(lista[2])
print('---------------------------')
print(lista)