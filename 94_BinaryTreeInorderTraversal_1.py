# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root):
        """
        :param root: TreeNode
        :return: List[int]
        """
        result = []

        if root:

            result = self.inorderTraversal(root.left)

            result.append(root.val)

            result = result + self.inorderTraversal(root.right)

        return result
