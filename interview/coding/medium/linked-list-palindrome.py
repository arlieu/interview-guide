'''Determine if a linked list, which represents a string (one letter per node), is a palindrome in one iteration.'''


# Solution 1: Singly linked list with head pointer
'''
from data_structures.linked_lists.singly_linked import *


def palindrome1(head):
    cur = head
    stack, queue = [], []
    while cur is not None:
        stack.append(cur.val)
        queue.append(cur.val)

    while 1:
        if not stack and not queue:
            return True

        if stack.pop() != queue.pop(0):
            return False
'''


# Solution 2: Doubly linked list with head and tail pointers
from data_structures.linked_lists.doubly_linked import *


def palindrome2(head, tail):
    while head and tail:
        if head.val != tail.val:
            return False
        head = head.next
        tail = tail.prev

    return True