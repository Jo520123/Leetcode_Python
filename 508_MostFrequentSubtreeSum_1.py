from collections import Counter
#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findFrequentTreeSum(self, root):
        """
        :param root: TreeNode
        :return: List[int]
        """
        if root is None:
            return []

        v = []
        self.total(root, v)

        freq = Counter(v)
        max_freq = max(freq.values())

        ans = []

        for i, j in freq.items():
            if j == max_freq:
                ans.append(i)

        return ans


    def total(self, root, x):
        
        if root is None:
            return 0

        n = self.total(root.left, x) + root.val + self.total(root.right, x)

        x.append(n)

        return n
