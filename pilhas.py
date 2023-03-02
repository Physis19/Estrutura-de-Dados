class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self._size = 0
    
    def push(self, elem):
        node = Node(elem)
        node.next = self.top
        self.top = node
        self._size += 1
        
    
    def pop(self):
        if self._size > 0:
            node = self.top
            self.top = self.top.next
            self._size -= 1
            return node

    def peek(self):
        if self._size > 0:
           return self.top.data

    def __len__(self):
        return self._size

    def __repr__(self):
        r = ""
        pointer = self.top
        while(pointer):
            r = r + str(pointer.data) + "\n"
            pointer = pointer.next
        return r
        
    def __str__(self):
        return self.__repr__()


fila = Stack()
fila.push(1)
fila.push(2)
fila.push(3)
print('==================')
print(fila)
print(f'Tamanho da nossa fila {len(fila)}')
fila.pop()
print('==================')
print(fila)
print(f'Tamanho da nossa fila {len(fila)}')
print('==================')