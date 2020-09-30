class Solution():
    def maxSubArrayLen(self, nums, k):
        """
        :param nums: List[int]
        :param k: int
        :return: int
        """
        table = {}

        sum, maxl = 0, 0
        l = len(nums)

        for i in range(l):

            sum += nums[i]

            if (sum == k):
                maxl = i + 1

            elif (sum -k) in table:
                maxl = max(maxl, i - table[sum -k])

            else:
                table[sum] = i

        return maxl
