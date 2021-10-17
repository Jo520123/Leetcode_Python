#Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def removeLeafNodes(self, root, target):
        """
        :param root: Optional[TreeNode]
        :param target: int
        :return: Optional[TreeNode]
        """

        if root == None:
            return None

        l = self.removeLeafNodes(root.left, target)
        r = self.removeLeafNodes(root.right, target)

        if l == None:
            root.left = None

        if r == None:
            root.right = None


        if (l == None and r == None and root.val == target):

            return None

        else:
            return root
