import math

class Node:
    def __init__(self,d):
        self.data = d
        self.left = None
        self.right = None


def SortedArrayToBST(a):
    if not a:
        return None

    mid =math.floor(len(a)/2)

    root = Node(a[mid])

    root.left = SortedArrayToBST(a[:mid])

    root.right = SortedArrayToBST(a[mid+1:])
    return root

def PreOrder(node):
    if not node:
        return
    print(node.data)
    PreOrder(node.left)
    PreOrder(node.right)
