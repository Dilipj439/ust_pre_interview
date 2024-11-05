class CircularQueue:
    def __init__(self, max_size=5):
        self.queue = {}
        self.max_size = max_size
        self.start = 0
        self.end = 0
        self.size = 0

    def add_queue(self, value):
        if self.size == self.max_size:
            print(f"Queue is full. Removing the oldest element: {self.queue[self.start]}")
            self.start = (self.start + 1) % self.max_size
            self.size -= 1
        self.queue[self.end] = value
        self.end = (self.end + 1) % self.max_size
        self.size += 1
        print(f"Added {value} to the queue. Current queue: {self.queue}")

    def display(self):
        print("Queue contents in order:")
        index = self.start
        for _ in range(self.size):
            print(self.queue[index], end=" ")
            index = (index + 1) % self.max_size
        print("\n")

def circular_queue_dic():
    cq = CircularQueue()

    cq.add_queue(1)
    cq.add_queue(2)
    cq.add_queue(3)
    cq.add_queue(4)
    cq.add_queue(5)
    cq.display()

    print("removing the first queue")

    cq.add_queue(6)
    cq.display()

