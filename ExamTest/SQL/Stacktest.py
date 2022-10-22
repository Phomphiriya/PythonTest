class Stack:
    def __init__(self,items = None):
        if items == None:
            self.items = []
        else:
            self.items = items
    def __str__(self):
        return str(self.items)
    def push(self,i):
        self.items.append(i)
    def pop(self):
        self.items.pop()
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)
    def peek(self):
        return self.items[-1]
    def bottom(self):
        return self.items[0]
    
inp = input("Enter input: ")
s = Stack()