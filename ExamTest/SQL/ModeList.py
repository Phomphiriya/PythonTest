class Node:
    def __init__(self, data, next = None, prev = None):
        self.data = data
        if next is None:
            self.next = None
        else:
            self.next = next
        if prev is None:
            self.prev = None
        else:
            self.prev = prev

    def __str__(self):
        return str(self.data)

class DoublyLk:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        curr = self.head
        strt = ""
        if curr == None:
            return strt + "Empty"
        else:
            while curr != None:
                strt += str(curr.data) + " "
                curr = curr.next
            return strt

    def isEmpty(self):
        return self.head == None

    def size(self):
        curr = self.head
        if self.isEmpty():
            return "Empty"
        else:
            count = 0
            while curr != None:
                curr = curr.next
                count += 1
            return count
    
    def addHead(self, data):
        p = Node(data)
        if self.isEmpty():
            self.append(data)
        else:
            p.next = self.head
            self.head.prev = p
            self.head = p

    def append(self, data):
        p = Node(data)
        if self.isEmpty():
            self.head = p
            self.tail = p
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            p.prev = self.tail
            self.tail.next = p
            self.tail = p
    
    def appendSort(self, data):
        i = int(data)
        p = Node(i)
        if self.isEmpty() or self.head.data >= data:
            self.addHead(i)
        else:
            curr = self.head
            while curr.next != None:
                if curr.next.data >= data:
                    break
                else:
                    curr = curr.next
            if curr.next == None:
                p.prev = curr
                curr.next = p
                self.tail = p
            else:
                p.next = curr.next
                p.prev = curr
                curr.next.prev = p
                curr.next = p

    def findMode(self):
        mem = {}
        if self.isEmpty():
            return "Empty"
        else:
            curr = self.head
            while curr != None:
                ls1 = list(mem.keys())
                if curr.data in ls1:
                    mem[curr.data] += 1
                else:
                    d = {curr.data: 1}
                    mem.update(d)
                curr = curr.next
            ls1 = list(mem.keys())
            ls2 = list(mem.values())
            maxValue = []
            maxT = 0
            for i in mem:
                if mem[i] > maxT:
                    maxT = mem[i]
                else:
                    pass
            for i in mem:
                if mem[i] == maxT:
                    maxValue.append(i)
                else:
                    pass
            return maxValue

lk = DoublyLk()
inp = input("Enter input : ").split()
for i in inp:
    i = int(i)
    lk.appendSort(i)
print(f'Output : {lk}')
print(f'Amount of data = {lk.size()}')
print(f'Mode : {lk.findMode()}')