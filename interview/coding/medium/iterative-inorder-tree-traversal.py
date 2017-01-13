'''Write an algorithm for inorder traversal of a BST without recursion.
Recursive solution:
    res = []
    def inorder(root):
        inorder(root.left)
        res.append(root.val)
        inorder(root.right)
'''


def inorder(root):
    res, stack = [], []
    current = root

    while 1:
        while current is not None:
            stack.append(current)
            current = current.left

        if len(stack) == 0:
            return res

        tmp = current
        res.append(tmp.val)
        current = tmp.right

    return res