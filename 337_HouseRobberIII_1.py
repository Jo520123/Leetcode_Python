# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root):
        """
        :param root:  TreeNode
        :return: int
        """
        return max(self.DFS(root))

    def DFS(self, root):
        if root is None:
            return (0, 0)

        l, r = self.DFS(root.left), self.DFS(root.right)
        rob_par = root.val +l[1] + r[1]
        rob_chi = max(l) + max(r)
        return (rob_par, rob_chi)

