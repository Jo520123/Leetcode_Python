"""
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
"""
class Solution(object):
    def MaxDepth(self,r):
        """"
            :type r:TreeNode
            :rtype:int
            """
        return self.solve(r)
    def solve(self,r,depth=0):
        if r == None:
            return depth
        return max(self.solve(r.left,depth+1),self.solve(r.right,depth+1))






