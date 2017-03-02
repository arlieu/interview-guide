from algorithms.sorting.efficient.heapsort import heapsort


class PriorityQueue:
    def __init__(self):
        self.priorityQueue = []

    def __init__(self, array):
        self.priorityQueue = heapsort(array)

    def insert(self, value):
        self.priorityQueue.append(value)
        self.priorityQueue = heapsort(self.priorityQueue)

    def pop(self):
        if len(self.priorityQueue) == 0:
            return

        return self.priorityQueue.pop()

    def peek(self):
        return self.priorityQueue[-1]