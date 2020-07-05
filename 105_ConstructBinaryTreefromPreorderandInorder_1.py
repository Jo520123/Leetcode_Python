# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :param preorder: List[int]
        :param inorder: List[int]
        :return: TreeNode
        """
        if not preorder and not inorder:
            return None


        root_v = preorder[0]
        root = TreeNode(root_v)
        inorder_ide = inorder.index(root_v)

        root.left = self.buildTree(preorder[1: inorder_ide+1], inorder[:inorder_ide])
        root.right = self.buildTree(preorder[inorder_ide+1:], inorder[inorder_ide+1:])

        return root

