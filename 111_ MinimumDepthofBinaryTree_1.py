class Node:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def MinDepth(self,root):
        """"
            :type root :TreeNode
            :rtype:int
            """
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1

        if root.left is None:
            return self.MinDepth(root.right)+1


        if root.right is None:
            return self.MinDepth(root.left) +1

        return min(self.MinDepth(root.left), self.MinDepth(root.right))+1

