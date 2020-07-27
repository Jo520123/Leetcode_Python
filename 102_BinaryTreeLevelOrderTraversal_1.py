#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root):
        """
        :param root: TreeNode
        :return: List[List[int]]
        """
        r = []
        h = self.height(root)
        for i in range(1, h+1):
            r.append([])
            self.Level(root, i,r, 0)
        return r



    def Level(self, root, l, r, c):
        if root is None:
            return


        if l == 1 :
            r[c].append(root.val)

        elif l > 1:
            self.Level(root.left, l - 1, r, c + 1)
            self.Level(root.right, l - 1, r, c + 1)

        return r


    def height(self, root):
        if root is None:
            return 0

        else:
            l = self.height(root.left)
            r = self.height(root.right)

        if l > r:
            return l + 1
        else:
            return r + 1
