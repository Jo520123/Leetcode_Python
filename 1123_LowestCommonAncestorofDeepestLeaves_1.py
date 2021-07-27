# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lcaDeepestLeaves(self, root):
        """
        :param root: TreeNode
        :return: TreeNode
        """
        self.lea = []
        self.listnode = []

        self.DFS(root)

        M = max([len(x) for x in self.listnode])

        self.listnode = [x for x in self.listnode if len(x) == M]

        if len(self.listnode) == 1:
            return self.listnode[0][-1]

        for i in range (M):
            for j in range(1, len(self.listnode)):
                if self.listnode[0][i] != self.listnode[j][i]:
                    return self.listnode[1][i-1]


    def DFS(self,root):
        if not root.left and not root.right:
            self.lea.append(root)
            self.listnode.append(list(self.lea))
            self.lea.pop()
            return

        if root.left:
            self.lea.append(root)
            self.DFS(root.left)
            self.lea.pop()

        if root.right:
            self.lea.append(root)
            self.DFS(root.right)
            self.lea.pop()
