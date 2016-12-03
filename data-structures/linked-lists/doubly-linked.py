class Node:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.cnt = 0

    def addHead(self, x):
        node = Node(x)

        if self.cnt == 0:
            self.head = node
            self.tail = self.head

        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

        self.cnt += 1

    def addTail(self, x):
        node = Node(x)

        if self.cnt == 0:
            self.head = node
            self.tail = self.head

        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = self.tail.next

        self.cnt += 1

    def removeHead(self):
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

    def removeTail(self):
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

    def size(self):
        return self.cnt

    def printForward(self):
        cur = self.head

        while cur is not None:
            print(cur.val, end=" ")
            cur = cur.next

        print("")

    def printReverse(self):
        cur = self.tail

        while cur is not None:
            print(cur.val, end = " ")
            cur = cur.prev

        print("")