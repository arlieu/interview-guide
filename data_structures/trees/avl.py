class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None


class AVL:
    def __init__(self):
        self.root = None
        self.height = -1
        self.balance = 0

    def insert(self, val):
        node = Node(val)

        if self.root is None:
            self.root = node
            self.root.left = AVL()
            self.root.right = AVL()

        elif val > self.root.value:
            self.root.right.insert(val)

        elif val < self.root.value:
            self.root.left.insert(val)

        else:
            print("Value already in AVL Tree")
            return

        self.updateHeight(False)
        self.updateBalance(False)
        self.rebalance()

    def updateHeight(self, recursive=True):
        if self.root:
            if recursive:
                if self.root.left:
                    self.root.left.updateHeight()
                if self.root.right:
                    self.root.right.updateHeight()

            self.height = 1 + max(self.root.left.height, self.root.right.height)
        else:
            self.height = -1

    def updateBalance(self, recursive=True):
        if self.root:
            if recursive:
                if self.root.left:
                    self.root.left.updateBalance()
                if self.root.right:
                    self.root.right.updateBalance()

            self.balance = self.root.left.height - self.root.right.height
        else:
            self.balance = 0

    def rebalance(self):
        if self.balance > 1:
            if self.root.left.balance < 0:
                # Left, right case
                self.root.left.rotateLeft()
                self.updateHeight()
                self.updateBalance()

            # Left, left case
            self.rotateRight()
            self.updateHeight()
            self.updateBalance()

        if self.balance < -1:
            if self.root.right.balance > 0:
                # Right, left case
                self.root.right.rotateRight()
                self.updateHeight()
                self.updateBalance()

            # Right, right case
            self.rotateLeft()
            self.updateHeight()
            self.updateBalance()

    def rotateRight(self):
        new_root = self.root.left.root
        sub_left = new_root.right.root
        old_root = self.root
        self.root = new_root
        old_root.left.root = sub_left
        new_root.right.root = old_root

    def rotateLeft(self):
        new_root = self.root.right.root
        sub_right = new_root.left.root
        old_root = self.root
        self.root = new_root
        old_root.right.root = sub_right
        new_root.left.root = old_root

    def remove(self, val):
        if self.root.value == val:
            # Leaf
            if not self.root.left.root and not self.root.right.root:
                self.root = None
            # Right subtree only
            elif not self.root.left.root and self.root.right.root:
                self.root = self.root.right.root
            # Left subtree only
            elif self.root.left.root and not self.root.right.root:
                self.root = self.root.left.root
            # Left and right subtree
            else:
                new_subroot = self.root.right.root
                while new_subroot and new_subroot.left.root:
                    new_subroot = new_subroot.left.root

                if new_subroot:
                    self.root.value = new_subroot.value
                    self.root.right.remove(new_subroot.value)
        elif val > self.root.value:
            self.root.right.remove(val)
        elif val < self.root.value:
            self.root.left.remove(val)
        else:
            print("Value not in AVL Tree")
            return

        self.rebalance()

    def preOrder(self):
        self.__preOrder(self.root)
        print("")

    def __preOrder(self, node):
        if node:
            print(node.value, end=" ")
            self.__preOrder(node.left.root)
            self.__preOrder(node.right.root)

    def inOrder(self):
        self.__inOrder(self.root)
        print("")

    def __inOrder(self, node):
        if node:
            self.__inOrder(node.left.root)
            print(node.value, end=" ")
            self.__inOrder(node.right.root)

    def postOrder(self):
        self.__postOrder(self.root)
        print("")

    def __postOrder(self, node):
        if node:
            self.__postOrder(node.left.root)
            self.__postOrder(node.right.root)
            print(node.value, end=" ")