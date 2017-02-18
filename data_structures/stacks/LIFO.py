class Stack:
    def __init__(self):
        self.stack = []
        self.cnt = 0

    def push(self, x):
        self.stack.append(x)
        self.cnt += 1

    def pop(self):
        self.stack.pop()
        self.cnt -= 1

    def peek(self):
        return self.stack[-1]

    def empty(self):
        return self.cnt == 0

    def size(self):
        return self.cnt