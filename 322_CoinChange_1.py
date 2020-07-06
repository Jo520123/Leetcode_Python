class Solution:
    def coinChange(self, coins, amount):
        """
        :param coins: List[int]
        :param amount: int
        :return: int
        """
        methods = [0] + [-1] * amount

        for i in range(amount):
            if methods[i] < 0:
                continue

            for val in coins:
                if val + i > amount:
                    continue
                if methods[i + val] < 0 or methods[i + val] > methods[i] +1:
                    methods[i + val] = methods[i] + 1

        return methods[amount]
