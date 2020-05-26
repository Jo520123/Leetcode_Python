"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""

class Solution:
    def IsSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True

        if not q or not p:
            return False

        if p.val != q.val:
            return False

        return self.IsSameTree(p.right, q.right) and self.IsSameTree(p.left, q.left)

