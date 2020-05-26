class Solution:
    def ClimbStairs(self,n):
        """
        :type n:int
        :rtype: int
        """
        if n <=0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2

        result = [0]* (n+1)
        result[0:3] = [0,1,2]

        for i in range(3,n+1):
            result[i] = result[i-1]+result[i-2]
        return result[n]

