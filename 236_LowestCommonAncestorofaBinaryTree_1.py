# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root , p , q):
        """
        :param root: 'TreeNode'
        :param p: 'TreeNode'
        :param q: 'TreeNode'
        :return: 'TreeNode'
        """

        if root is None or p == root or q == root:
            return root
        l = self.lowestCommonAncestor(root.left, p,q)
        r = self.lowestCommonAncestor(root.right, p, q)

        if l and r :
            return root

        if l:
            return l
        else:
            return r
