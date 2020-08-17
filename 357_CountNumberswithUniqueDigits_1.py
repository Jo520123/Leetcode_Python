class Solution:
    def countNumbersWithUniqueDigits(self, n):
        """
        :param n: int
        :return: int
        """
        result = [9]
        if n == 0 :
            return 1

        for i in range(9, 0, -1):
            result.append((result[-1])*i)

        total = sum(result[:n])

        return total + 1
