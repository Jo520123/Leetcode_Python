# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root, sum):
        """
        :param root: TreeNode
        :param sum: int
        :return:  List[List[int]]
        """
        if root is None:
            return []

        output = []
        self.DFS(root, sum, output, [root.val])

        return output

    def DFS(self, root, s, output, p ):
        if root is None:
            return

        if sum(p) == s and root.left is None and root.right is None:
            output.append(p)
            return

        if root.left:
            self.DFS(root.left, s, output, p + [root.left.val])

        if root.right:
            self.DFS(root.right, s, output, p + [root.right.val])
