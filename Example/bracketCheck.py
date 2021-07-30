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

def isMatch(i,j):
    if i == "{" and j == "}":
        return True
    elif i == "(" and j == ")":
        return True
    elif i == "[" and j == "]":
        return True
    else:
        return False

inp = input("Enter bracket : ")
s=Stack()
openB = ["{","(","["]
closeB = [")","]","}"]

for i in inp:
    if i in openB:
        s.push(i)
    elif i in closeB:
        a = s.peek()
        if isMatch(a,i):
            s.pop()
    else:
        pass

if s.empty():
    print("Match")
else:
    print("Not match")