class Solution:
    def ArrangeCoins(self, x):
        """
        :type x: int
        :rtype: int
        """
        l, r = 0, x + 1
        while l < r:
            mid = l + (r - l) // 2
            if mid * (mid + 1) / 2 <= x:
                l = mid + 1
            else:
                r = mid
        return l - 1
