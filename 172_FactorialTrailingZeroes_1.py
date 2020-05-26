class Solution(object):
    def TrailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n > 0:
            n = int(n/5)
            res += n
        return res

