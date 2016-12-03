class Node:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None


class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.cnt = 0

    def pushFront(self, x):
        node = Node(x)

        if self.cnt == 0:
            self.head = node
            self.tail = self.head

        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

        self.cnt += 1

    def pushBack(self, x):
        node = Node(x)

        if self.cnt == 0:
            self.head = node
            self.tail = self.head

        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = self.tail.next

        self.cnt += 1

    def popFront(self):
        if self.cnt == 0:
            return

        elif self.cnt == 1:
            self.head = None
            self.tail = None

        else:
            self.head = self.head.next
            self.head.prev.next = None
            self.head.prev = None

        self.cnt -= 1

    def popBack(self):
        if self.cnt == 0:
            return

        elif self.cnt == 1:
            self.head = None
            self.tail = None

        else:
            self.tail = self.tail.prev
            self.tail.next.prev = None
            self.tail.next = None

        self.cnt -= 1

    def peekFront(self):
        if self.head is None:
            return

        return self.head.val

    def peekBack(self):
        if self.tail is None:
            return

        return self.tail.val

    def size(self):
        return self.cnt

    def empty(self):
        return self.cnt == 0