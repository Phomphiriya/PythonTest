class Stack:
    def __init__(self,items = None):
        if items == None:
            self.items =[]
        else:
            self.items = items
    
    def push(self,i):
        return self.items.append(i)
    
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

class Queue:
    def __init__(self,items = None):
        if items == None:
            self.items = []
        else:
            self.items = items
    
    def enQueue(self,i):
        return self.items.append(i)
    
    def deQueue(self):
        return self.items.pop(0)
    
    def isEmpty(self):
        return self.items ==[]
    
    def size(self):
        return len(self.items)
    
    def head(self):
        return self.items[0]
    
    def __str__(self):
        return str(self.items)

inp = input("Enter input : ")
s = Stack()
q = Queue()
i = len(inp)//2
o = 0

for j in inp:
        s.push(inp[o])
        q.enQueue(inp[o])
        o += 1
        
check = True
while i > 0:
    if q.head() == s.peek():
        s.pop()
        q.deQueue()
        check = True
    else:
        check = False
        break
    i -= 1
if check == True:
    print("It's palindrom")
else:
    print("It isn't palindrom")
print(q.head())
print(s.peek())
print(s)
print(q)
print(len(inp))
