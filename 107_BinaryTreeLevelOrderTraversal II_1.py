"""
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
"""
class Solution(object):
    def LevelOrderBottom(self,r):
        """"
        :type r:TreeNode
        :rtype: List[List[int]]
        """
        if r == None:
            return []

        res = []
        nodes = [r]
        while nodes:
            res.append([node.val for node in nodes])
            next_node =[]
            for node in nodes:
                if node.left:
                    next_node.append(node.left)
                if node.right:
                    next_node.append(node.right)
            nodes = next_node
        return res[::-1]


