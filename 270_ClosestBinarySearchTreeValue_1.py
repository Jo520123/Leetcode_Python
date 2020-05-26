class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def ClosestValue(self, root, target):
        """
        :param root: TreeNode
        :param target: float
        :return: int
        """
        if root is None:
            return float('inf')

        if root.val == target:
            return root.val

        elif root.val < target:
            right_res = self.ClosestValue(root.right, target)
            return root.val if abs(root.val - target) < abs(right_res - target) else right_res

        elif root.val > target:
            left_res = self.ClosestValue(root.left, target)
            return root.val if abs(root.val - target) < abs(left_res - target) else left_res


