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
class PriorityNode():
    def __init__(self,data=None,priority=None,next=None):
        self.data=data
        self.priority=priority
        self.next=next
class PriorityQueue():
    def __init__(self):
        self.front=None
        self.rear=None
        self.size=0
    def clear(self):
        self.front=None
        self.rear=None
        self.size=0
    def isEmpty(self):
        return self.size==0
    def length(self):
        return self.size
    def peek(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        return self.front.data
    def offer(self,data,priority):
        new_node=PriorityNode(data,priority)
        if self.isEmpty():
            self.front=new_node
            self.rear=new_node
        else:
            current=self.front
            previous=None
            while current and current.priority<=priority:
                previous=current
                current=current.next
            if previous is None:
                new_node.next=self.front
                self.front=new_node
            else:
                previous.next=new_node
                new_node.next=current
                if current is None:
                    self.rear=new_node
        self.size+=1
    def poll(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        item=self.front.data
        self.front=self.front.next
        if self.front is None:
            self.rear=None
        self.size-=1
        return item
    def display(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        current=self.front
        while current:
            print(f"({current.data},{current.priority})",end=' ')
            current=current.next
        print()
class ApplyExample():
    def processadmin(self,PriorityQueue):#例3.7,课本p48
        '''处理任务的顺序是根据任务的优先级来决定的，优先级高的任务先处理，优先级低的任务后处理。'''
        pq=PriorityQueue()
        pq.offer("任务1",3)
        pq.offer("任务2",1)
        pq.offer("任务3",2)
        pq.offer("任务4",4)
        print("任务处理顺序为：")
        while not pq.isEmpty():
            task=pq.poll()
            print(task,end=' ')