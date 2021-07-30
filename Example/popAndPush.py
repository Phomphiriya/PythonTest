class Stack:
    def __init__(self,items = None):

        if items == None:
            self.items = []
        else:
            self.items = items

    def isEmpty(self):
        # if self.items == []:
        #     return True
        # else:
        #     return False
        return self.items == []
    
    def size(self):
        # a = len(self.items)
        # return a
        return len(self.items)

    def push(self,i):
        self.items.append(i)
    
    def pop(self):
        a = self.items.pop()
        return a

    def peek(self):
        return self.items[-1]

    def __str__(self):
        return str(self.items)

# A 20,A 10,A 30,P

inp = input("Enter : ").split(',')
s = Stack()
for i in inp:
    a = i.split()
    if a[0] == 'A':
        s.push(a[1])
        print(s)
    else:
        s.pop()
        print(s)