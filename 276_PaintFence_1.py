class Solution:
    def Numways(self, x, y):
        """
        :param x: int
        :param y: int
        :return: int
        """
        if x == 0:
            return 0
        else:
            if y ==0:return 0
            elif x == 1 : return y
            elif x ==2 : return y*y
            else:
                dp = [0 for i in range(x+1)]
                dp[0] = 0
                dp[1] = y
                dp[2] = y*y

                for i in range(3,x+1):
                    dp[i] = (y-1) * dp[i-1] + (y-1) * dp[i-2]
                return dp[-1]

