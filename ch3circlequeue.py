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