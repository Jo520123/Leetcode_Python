# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :param root: TreeNode
        :return: List[List[int]]
        """
        if root is None:
            return []

        que, result = [(root, 1)], []

        while que != []:
            node, layer = que.pop(0)
            if node.left != None:
                que.append([ node.left, layer+1])

            if node.right != None:
                que.append([node.right, layer + 1])

            if layer == len(result):
                result[layer-1].append(node.val)
            else:
                result.append([node.val])


        for i in range(len(result)):
            if i %2 == 1:
                result[i] = result[i][::-1]

        return result
