class Solution:
    def MinCost(self, cost):
        if not cost: return 0

        dp = cost[0][:]
        for i in range(1,len(cost)):
            pre = dp[:]
            for j in range(len(cost[0])):
                dp[j] = cost[i][j] + min(pre[:j] + pre[j+1:])
        return min(dp)
