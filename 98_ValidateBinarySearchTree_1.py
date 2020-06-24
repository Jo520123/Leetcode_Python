#Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0):
         self.val = val
         self.left = None
         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :param root: TreeNode
        :return: bool
        """
        return self.effective(root, float('-inf'), float('inf'))

    def effective(self, root, min, Max):
        if not root:
            return True

        if root.val <= min or root.val >= Max:
            return False

        return self.effective(root.left, min, root.val) and self.effective(root.right, root.val , Max)


