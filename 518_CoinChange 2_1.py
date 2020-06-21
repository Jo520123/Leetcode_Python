class Solution:
    def change(self, amount, coins):
        """
        :param amount: int
        :param coins: List[int]
        :return: int
        """
        total_amount = amount + 1
        combin = [0] * (total_amount)
        combin[0] = 1

        for i in coins:
            for j in range(1, total_amount):
                if j >= i:
                    combin[j] += combin[j-i]

        return combin[amount]
