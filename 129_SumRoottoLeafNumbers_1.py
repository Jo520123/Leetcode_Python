# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root):
        """
        :param root: TreeNode
        :return:int
        """
        return self.DFS(root,0)


    def DFS(self, root, sum):
        if root is None:
            return 0

        sum = sum*10 + root.val

        if root.left is None and root.right is None:
            return sum

        return self.DFS(root.left, sum) + self.DFS(root.right, sum)
