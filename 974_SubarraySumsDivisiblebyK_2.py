from collections import defaultdict
class Solution:
    def subarraysDivByK(self, A, K):
        """
        :param A: List[int]
        :param K: int
        :return: int
        """

        table = defaultdict(int)
        table[0] = 1
        total = 0
        result = 0

        for x in A:
            total += x
            m = total % K
            result += table[m]
            table[m] += 1

        return result
