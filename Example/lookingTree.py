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

def lookingTree(s):
    scopy  = s.items.copy()
    scopy = Stack(scopy)
    count = 0
    highest = 0
    while not scopy.empty():
        if scopy.peek() > highest:
            count += 1
            highest = scopy.peek()
            scopy.pop()
        else:
            scopy.pop()
    return count

inp = input("Enter input : ").split(',')
s = Stack()
for i in inp:
    if i == 'B':
        print(lookingTree(s))
    else:
        a = int(i)
        s.push(a)
print(s)

# Test case
# 1,6,3,2,B
# 3