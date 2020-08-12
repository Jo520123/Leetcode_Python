# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def insertIntoBST(self, root, val) :
        """
        :param root: TreeNode
        :param val: int
        :return: TreeNode
        """
        if root is None:
            n = TreeNode(val)
            return n

        if val < root.val:
            if root.left is None:
                root.left = TreeNode(val)
            else:
                self.insertIntoBST(root.left, val)

        elif val > root.val:
            if root.right is None:
                root.right = TreeNode(val)
            else:
                self.insertIntoBST(root.right, val)

        return root
