class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0

    def push(self, elem):
        node = Node(elem)
        if self.last is None:
            self.last = node
        else:
            self.last.next = node
            self.last = node

        if self.first is None:
            self.first = node

        self._size = self._size + 1
        
    
    def pop(self):
       if self._size > 0:
           elem = self.first.data
           self.first = self.first.next
           self._size -= 1
           return elem

    def peek(self):
        if self._size > 0:
           elem = self.first.data
           return elem

    def __len__(self):
        return self._size
        

    def __repr__(self):
       if self._size > 0:
        r = ''
        pointer = self.first
        while(pointer):
                r  = r + str(pointer.data) + " "
                pointer = pointer.next
        return r
        
    def __str__(self):
        return self.__repr__()

fila = Queue()
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
