class Solution:
    def ReverseBits(self, n):
        """
        :type  n: int
        :rtype: int
        """
        a = bin(n)[:1:-1]
        return int(a + '0'*(32-len(a)),2)
