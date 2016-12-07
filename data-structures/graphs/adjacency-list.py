class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.cnt = 0

    def addHead(self, x):
        node = Node(x)
        node.next = self.head
        self.head = node
        self.cnt += 1

    def addTail(self, x):
        node = Node(x)

        if self.head is None:
            self.head = node

        else:
            cur = self.head

            while cur.next is not None:
                cur = cur.next

            cur.next = node

        self.cnt += 1

    def removeHead(self):
        if self.head is None:
            return

        self.head = self.head.next
        self.cnt -= 1

    def removeTail(self):
        if self.head is None:
            return

        cur = self.head
        prev = cur

        while cur.next is not None:
            prev = cur
            cur = cur.next

        prev.next = None
        self.cnt -= 1

    def size(self):
        return self.cnt


def printForward(head):
    if head is None:
        return

    print(head.val)

    while head.next is not None:
        head = head.next
        print(head.val)


def printReverse(head):
    if head is None:
        return

    printReverse(head.next)

    print(head.val)


class AdjacencyList:
    def __init__(self, n):
        self.n = n
        self.ls = [None]*n

    def addEdge(self, start, end):
        if start < 0 or start > self.n-1:
            return

        if self.ls[start] is None:
            ll = LinkedList()
            ll.addTail(end)
            self.ls[start] = ll
        else:
            self.ls[start].addTail(end)

    def hasEdge(self, start, end):
        if start < 0 or start > self.n-1 or self.ls[start] is None:
            return False

        cur = self.ls[start].head
        while cur is not None and cur.val != end:
            cur = cur.next

        if cur is None:
            return False

        return cur.val == end

    def edgePaths(self, start):
        if start < 0 or start > self.n-1:
            return

        cur = self.ls[start].head

        print(str(start) + ": ", end="")

        if cur is not None:
            print("[" + str(cur.val), end = "")
            cur = cur.next

        while cur is not None:
            print(" " + str(cur.val), end="")
            cur = cur.next

        print("]")