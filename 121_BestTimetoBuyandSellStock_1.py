class Solution:
    def MaxProfit(self, prices):
        """
        :type prices: List
        :rtype int
        """
        Max_price = 0

        for i in range(0,len(prices)-1):
            for j in range(i+1,len(prices)):
                profit = prices[j]-prices[i]
                if profit > Max_price:
                    Max_price = profit
        return Max_price
