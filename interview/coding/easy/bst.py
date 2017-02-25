'''Implement a basic BST with insertion and find capabilities.'''


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = Node(val)

        return self.__insert(self.root, val)

    def __insert(self, node, val):
        if node is None:
            node = Node(val)
        elif node.val > val:
            node.left = self.__insert(node.left, val)
        elif node.val < val:
            node.right = self.__insert(node.right, val)

        return node

    def find(self, val):
        if self.root and self.root.val == val:
            return True

        return self.__find(self.root, val)

    def __find(self, node, val):
        if not node:
            return False
        elif node.val == val:
            return True
        elif node.val > val:
            return self.__find(node.left, val)
        else:
            return self.__find(node.right, val)