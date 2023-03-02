class Hashtable:
    def __init__(self) -> None:
        self.max = 100
        self.arr = [None for i in range(self.max)]
    
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.max
    

