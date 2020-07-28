from collections import deque
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def rightSideView(self, root):
        """
        :param root: TreeNode
        :return: List[int]
        """
        r = []
        if root is None:
            return r

        q = deque()
        q.append(root)

        while q:
            r.append(q[-1].val)
            for i in range(len(q)):
                n = q.popleft()
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)

        return r
