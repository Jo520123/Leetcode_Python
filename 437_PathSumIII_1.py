class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def PathSum(self,root, sum):
        """
                :type root: TreeNode
                :type sum: int
                :rtype: int
                """
        if not root :
            return 0
        return self.dfs(root,sum) + self.PathSum(root.left, sum) +self.PathSum(root.right, sum)

    def dfs(self,root , sum ):
        r = 0
        if not root:
            return r
        sum -= root.val
        if sum == 0:
            r +=1
        r += self.dfs(root.left, sum)
        r += self.dfs(root.right, sum)
        return r

