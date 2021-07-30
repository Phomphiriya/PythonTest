class Stack:
    def __init__(self,items = None):
        if items == None:
            self.items = []
        else:
            self.items = items
    
    def push(self,o):
        self.items.append(o)

    def pop(self):
        return self.items.pop()
    
    def empty(self):
        return self.items == []

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

inp = input("Enter input : ").split(',')
s = Stack()

for i in inp:
    if int(i) % 2 == 0:
        s.push(i)    
print(s)