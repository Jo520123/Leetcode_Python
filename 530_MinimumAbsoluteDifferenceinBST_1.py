# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root):
        """
        :param root: TreeNode
        :return: int
        """
        result = []
        self.Inorder(root, result)

        min_absd = float('inf')
        for i in range(1, len(result)):
            min_absd = min(min_absd, abs(result[i]-result[i-1]))

        return min_absd


    def Inorder(self, root ,result):
        if root is None:
            return
        else:
            self.Inorder(root.left, result)
            result.append(root.val)
            self.Inorder(root.right, result)
