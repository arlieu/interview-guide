class Queue:
    def __init__(self):
        self.queue = []
        self.cnt = 0

    def enqueue(self, x):
        self.queue.insert(0,x)
        self.cnt += 1

    def dequeue(self):
        self.queue.pop()
        self.cnt -= 1

    def peek(self):
        return self.queue[-1]

    def empty(self):
        return self.cnt == 0

    def size(self):
        return self.cnt