class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity

    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity
            self.queue[self.rear] = item
            self.size += 1
        else:
            raise OverflowError("Queue is Full")

    def dequeue(self):
        if not self.isEmpty():
            item = self.queue[self.front]
            self.front = (self.front + 1) % self.capacity
            self.size -= 1
            return item
        else:
            raise IndexError("dequeue from empty queue")

    def getSize(self):
        return self.size


queue = Queue(5)

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Queue:", queue.queue[:queue.getSize()])  # Output: [1, 2, 3]
print("Size:", queue.getSize())  # Output: 3

dequeued_item = queue.dequeue()
print("Dequeued item:", dequeued_item)  # Output: 1
print("Size:", queue.getSize())
print("Queue after dequeue:", queue.queue[queue.front:(queue.front + queue.getSize())])
