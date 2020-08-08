class Solution:
    def grayCode(self, n):
        """
        :param n: int
        :return: List[int]
        """
        if n < 0:
            return [0]

        if n == 1:
            return [0,1]


        result = self.grayCode(n-1)

        power_2 = int(2**(n-1))

        for i in range(power_2-1, -1, -1):
            result.append(result[i] + power_2)

        return result
