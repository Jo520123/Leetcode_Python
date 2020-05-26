class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def SumOfLeftLeaves(self, root):
        """
               :type root: TreeNode
               :rtype: int
               """
        a = 0
        if root:
            l, r = root.left, root.right
            if l and (l.left or l.right) is None:
                a += l.val
            a += self.SumOfLeftLeaves(l) + self.SumOfLeftLeaves(r)
        return a


