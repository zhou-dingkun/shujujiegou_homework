class CircleQueue():
    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = [None] * max_size
        self.front = 0
        self.rear = 0
        self.size = 0
    def clear(self):
        self.front = 0
        self.rear = 0
        self.size = 0
    def isEmpty(self):
        return self.rear == self.front
    def length(self):
        return self.size
        #也可以直接用rear-front来表示长度，但是当rear<front时，rear-front为负数，所以需要加上max_size
        #或者rear-front后取绝对值
    def peek(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        return self.queue[self.front]
    def offer(self,item):
        if (self.rear+1) % self.max_size == self.front:
            raise Exception("Queue is full")
        self.queue[self.rear] = item
        self.rear = (self.rear + 1) % self.max_size
        self.size += 1
    def poll(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        item = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.max_size
        self.size -= 1
        return item
    def display(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        index = self.front
        while index != self.rear:
            print(self.queue[index], end=' ')
            index = (index + 1) % self.max_size
        print()
class Node():
    def __init__(self, data=None,next=None):
        self.data = data
        self.next = next
class LinkedQueue():
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
    def clear(self):
        self.front = None
        self.rear = None
        self.size = 0
    def isEmpty(self):
        return self.size == 0
    def length(self):
        return self.size
    def peek(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        return self.front.data
    def offer(self, item):
        new_node = Node(item)
        if self.isEmpty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1
    def poll(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        item = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        return item
    def display(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        current = self.front
        while current:
            print(current.data, end=' ')
            current = current.next
        print()