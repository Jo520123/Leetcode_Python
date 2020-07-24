# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder , postorder):
        """
        :param inorder: List[int]
        :param postorder: List[int]
        :return: TreeNode
        """
        if not inorder or not postorder:
            return None

        p_root = postorder[-1]
        root = TreeNode(p_root)
        idx_inord = inorder.index(p_root)
        root.left = self.buildTree(inorder[:idx_inord], postorder[:idx_inord])
        root.right = self.buildTree(inorder[idx_inord+1:], postorder[idx_inord:-1])
        return root
