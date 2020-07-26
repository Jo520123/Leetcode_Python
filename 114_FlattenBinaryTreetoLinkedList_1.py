# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root):
        """
        :param root:  TreeNode
        :return: None
        """
        pointer = TreeNode(None)
        stack = [root]

        while stack:
            root = stack.pop()
            if root is None:
                continue
            stack.append(root.right)
            stack.append(root.left)
            pointer.right = root
            pointer.left = None
            pointer = root
