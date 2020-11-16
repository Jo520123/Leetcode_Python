from collections import Counter
class Solution:
    def numSubarraysWithSum(self, A, S):
        """
        :param A: List[int]
        :param S: int
        :return: int
        """
        le = len(A) + 1
        total = 0
        ans = 0
        sum_count = Counter({0:1})

        for i in range(1, le):
            total += A[i-1]
            ans += sum_count[total-S]
            sum_count[total] += 1

        return ans

