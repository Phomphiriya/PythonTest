class Queue:
    def __init__(self,items = None):
        if items == None:
            self.items = []
        else:
            self.items = items
    
    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)
    
    def head(self):
        return self.items[0]
    
    def deQueue(self):
        return self.items.pop(0)
    
    def enQueue(self,i):
        return self.items.append(i)
    
    def __str__(self):
        return str(self.items)

inp = input("Enter input : ").split(',')
q = Queue()

# A 10, A 20, P 40
for i in inp:
    a = i.split(' ')
    if a[0] == 'A':
        q.enQueue(a[1])
        print(q)
        print(q.size())
    else:
        print(q.deQueue())

