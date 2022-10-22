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
    
    def reverseStr(self):
        curr = self.tail
        strt = ""
        if curr == None:
            return strt + "Empty"
        else:
            while curr.prev != None:
                strt += str(curr.data) + " "
                curr = curr.prev
            strt += str(curr.data)
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
    
    def addHead(self, data):
        p = Node(data)
        if self.isEmpty():
            self.append(data)
        else:
            p.next = self.head
            self.head.prev = p
            self.head = p

    def pop(self, pos = None):
        if self.isEmpty():
            return "empty"
        else:
            if pos == None or pos == self.size() - 1:
                curr = self.tail.prev
                self.tail.prev.next = None
                self.tail = curr
            elif pos == 0:
                curr = self.head.next
                self.head.next = None
                curr.prev = None
                self.head = curr
            else:
                curr = self.head
                count = 0
                if pos > self.size():
                    return "Cant pop that items."
                else:
                    while count != pos:
                        curr = curr.next
                        count += 1
                    curr.next.prev = curr.prev
                    curr.prev.next = curr.next
                    curr.next == None
                    curr.prev == None

dlk = DoublyLk()
inp = list(map(int,input("Enter number : ").split()))
for i in inp:
    dlk.append(i)
print(dlk)
print(dlk.reverseStr())