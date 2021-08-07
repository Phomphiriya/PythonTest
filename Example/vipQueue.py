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
    
    def enQueueInsert(self,index,i):
        self.items.insert(index,i)
    
    def __str__(self):
        return str(self.items)


inp = input("Enter input : ").split(',')
q = Queue()
o = 0
for i in inp:
    a = i.split()
    if a[0] == 'EA':
        q.enQueue(a[1])  
    if a[0] == 'ES':
        q.enQueueInsert(o,a[1])
        o += 1
    print(q)

# Test case
# EA 10,ES 2,EA 20,EA 30,ES 5,ES 6,EA 50
# ['2', '5', '6', '10', '20', '30', '50']