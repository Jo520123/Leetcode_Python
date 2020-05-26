class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def Height(self,root):
        if root == None:
            return True
        return max(self.Height(root.left),self.Height(root.right)) + 1

    def IsBalance(self, root):
        """
        :type root: TreeNode
        :rtype:bool
        """
        if root == None:
            return True
        elif abs(self.Height(root.left) - self.Height(root.right)) <= 1:
            return self.IsBalance(root.left) and self.IsBalance(root.right)
        else:
            return False
