class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def InvertTree(self,root):
        if root is None:
            return None
        root.left, root.right = self.InvertTree(root.right), self.InvertTree(root.left)

        return root

