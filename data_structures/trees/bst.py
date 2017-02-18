class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            newNode = Node(val)
            self.root = newNode

        else:
            self.__insert(self.root, val)

    def __insert(self, node, val):
        if node is None:
            newNode = Node(val)
            node = newNode

        elif node.val > val:
            node.left = self.__insert(node.left, val)

        elif node.val < val:
            node.right = self.__insert(node.right, val)

        else:
            if node.val == val:
                print("Value already in BST")

        return node

    def remove(self, val):
        if self.root is None:
            print("Value not in BST")

        else:
            self.__remove(self.root, val)

    def __remove(self, node, val):
        if node is None:
            print("Value not in BST")
            return

        else:
            if node.val == val:
                if node.left is None and node.right is None:
                    return None

                elif node.left and node.right is None:
                    return node.left

                elif node.left is None and node.right:
                    return node.right

                else:
                    node.val = self.__findMin(node.right).val
                    self.__remove(node.right, node.val)
                    return node

            elif node.val > val:
                node.left = self.__remove(node.left, val)

            else:
                node.right = self.__remove(node.right, val)

    def find(self, val):
        if self.root is None:
            return False

        return self.__find(self.root, val)

    def __find(self, node, val):
        if node is None:
            return False

        elif node.val == val:
            return True

        elif node.val > val:
            return self.__find(node.left, val)

        else:
            return self.__find(node.right, val)

    def findMin(self):
        if self.root is None:
            return

        return self.__findMin(self.root)

    def __findMin(self, node):
        if node.left is None:
            return node

        return self.__findMin(node.left)

    def findMax(self):
        if self.root is None:
            return

        return self.__findMax(self.root)

    def __findMax(self, node):
        if node.right is None:
            return node

        return self.__findMax(node.right)

    def preOrder(self):
        if self.root is None:
            print("")

        else:
            self.__preOrder(self.root)
            print("")

    def __preOrder(self, node):
        if node is None:
            print("", end="")

        else:
            print(node.val, end=" ")
            self.__preOrder(node.left)
            self.__preOrder(node.right)

    def inOrder(self):
        if self.root is None:
            print("")

        else:
            self.__inOrder(self.root)
            print("")

    def __inOrder(self, node):
        if node is None:
            print("", end="")

        else:
            self.__inOrder(node.left)
            print(node.val, end=" ")
            self.__inOrder(node.right)

    def postOrder(self):
        if self.root is None:
            print("")

        else:
            self.__postOrder(self.root)
            print("")

    def __postOrder(self, node):
        if node is None:
            print("", end="")

        else:
            self.__postOrder(node.left)
            self.__postOrder(node.right)
            print(node.val, end=" ")
