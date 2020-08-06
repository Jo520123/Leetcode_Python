class Solution:
    def numSquares(self, n):
        """
        :param n: int
        :return: int
        """
        if n == 0:
            return 0

        result = [float('inf')] * (n+1)
        result[0] = 0
        result[1] = 1

        for i in range(2, n+1):
            x = 1
            while(x**2 <=i):
                result[i] = min(result[i], result[i-x**2]+1)
                x += 1

        return result[n]
