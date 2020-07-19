class Solution:
    def findMaxAverage(self, nums , k):
        """
        :param nums: List[int]
        :param k: int
        :return: float
        """
        r = float('-inf')
        total = 0

        for i, n in enumerate(nums):
            total += n
            if i >= k:
                total -= nums[i-k]

            if i >= k-1:
                r = max(r, total)

        r = r/k

        return r

