class LinkedList:
    class Node:
        def __init__(self, data, next=None):
            self.data = data
            if next is None:
                self.next = None
            else:
                self.next = next
        def __str__(self):
            return str(self.data)
    def __init__(self, head=None):
        if head == None:
            self.head = self.tail = None
            self.size = 0
        else:
            self.head = head
            t = self.head
            self.size = 1
            while t.next != None:
                t = t.next
                self.size += 1
            self.tail = t
    def __len__(self):
        return self.size
    def isEmpty(self):
        return self.size == 0
    def __str__(self):
        s = 'Queue data : '
        p = self.head
        if self.isEmpty():
            return "Empty Queue"
        while p != None:
            s += str(p.data) + ' '
            p = p.next
        return s
    def append(self, i):
        p = self.Node(i)
        if self.isEmpty():
            self.head = p
            self.tail = p
            self.size += 1
        else:
            self.tail.next = p
            self.tail = p
            self.size += 1
    def pop(self):
        if self.isEmpty():
            return
        else:
            self.head = self.head.next
            self.size -= 1
    
    # def popBack(self):
    #     if self.isEmpty():
    #         return
    #     else:
    #         t = self.head
    #         while t.next != self.tail:
    #             t = t.next
    #         self.tail = t
    #         t.next = None
    #         self.size -= 1

class Queue:
    def __init__(self, lis = None):
        if lis == None:
            self.items = LinkedList()
        else:
            self.items = lis
    
    def qIsEmpty(self):
        return self.items.isEmpty()
    
    def enQueue(self, i):
        self.items.append(i)
    
    def deQueue(self):
        self.items.pop()
    
    def size(self):
        return self.items.size
    
    def peek(self):
        return self.items.head
    
    def __str__(self):
        string = ""
        string += str(self.items)
        return string

# class Stack:
#     def __init__(self, lis = None):
#         if lis == None:
#             self.items = LinkedList()
#         else:
#             self.items = lis
    
#     def sIsEmpty(self):
#         return self.items.isEmpty()
    
#     def push(self, i):
#         self.items.append(i)
    
#     def pop(self):
#         self.items.popBack()

#     def peek(self):
#         return self.items.tail

#     def size(self):
#         return self.items.size
    
#     def __str__(self):
#         string = ""
#         string += str(self.items)
#         return string

# s = Stack()
inp = input('Enter choice : ')
q = Queue()

if inp == '1':
    q1 = Queue()
    q1.enQueue(10)
    q1.enQueue(20)
    q1.enQueue(30)
    print(q1)
    q1.deQueue()
    q1.enQueue(40)
    print("Size of Queue :",q1.size())
    print(q1)
elif inp == '2':
    q1 = Queue()
    q1.enQueue(100)
    q1.enQueue(200)
    q1.enQueue(300)
    q1.deQueue()
    print(q1)
    print("Queue is Empty :",q1.qIsEmpty())
else:
    q1 = Queue()
    q1.enQueue(11)
    q1.enQueue(22)
    q1.enQueue(33)
    q1.deQueue()
    q1.deQueue()
    q1.deQueue()
    print(q1)
    print("Size of Queue :",q1.size())
    print("Queue is Empty :",q1.qIsEmpty())