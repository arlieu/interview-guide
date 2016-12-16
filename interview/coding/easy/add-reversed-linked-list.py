'''Given two reversed linked lists, each representing one integer, add those two linked lists as if they were actual
correct ordered integers and return the result as a reversed linked list.
For example, L1: 0 -> 0 - > 1, L2: 0 -> 0 -> 2, ANS: 0 -> 0 -> 3.'''
class Node():
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None

    def append(self, x):
        newNode = Node(x)
        if self.head is None:
            self.head = newNode

        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next

            cur.next = newNode
            cur = cur.next

    def __iter__(self):
        cur = self.head
        while cur:
            yield cur.val
            cur = cur.next

    def __str__(self):
        res = ""
        if self.head is None:
            return res

        cur = self.head
        while cur.next is not None:
            res += str(cur.val) + " -> "
            cur = cur.next

        res += str(cur.val)
        return res


def addLists(num1, num2):
    res = LinkedList()
    carry = 0
    while num1.head or num2.head:
        if num1.head and num2.head:
            tmp = num1.head.val + num2.head.val + carry
            if tmp > 9:
                carry = tmp // 10
                tmp %= 10

            else:
                carry = 0

            res.append(tmp)
            num1.head = num1.head.next
            num2.head = num2.head.next

        elif num1.head:
            tmp = num1.head.val + carry
            if tmp > 9:
                carry = tmp // 10
                tmp %= 10

            else:
                carry = 0

            res.append(tmp)
            num1.head = num1.head.next

        elif num2.head:
            tmp = num1.head.val + carry
            if tmp > 9:
                carry = tmp // 10
                tmp %= 10

            else:
                carry = 0

            res.append(tmp)
            num2.head = num2.head.next

    if carry:
        res.append(carry)

    return res