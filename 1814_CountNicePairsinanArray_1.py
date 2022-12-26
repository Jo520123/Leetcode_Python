class Solution:
    def countNicePairs(self, nums):
        """
        :param nums:List[int]
        :return:int
        """

        l = len(nums)
        d = {}
        c = 0
        mod = 10**9 + 7

        for i in range(l):
            dv = nums[i] - int(str(nums[i])[::-1])

            d[dv] = d.get(dv,0) + 1

            if d[dv] > 1:
                c += d[dv] - 1

        return c % mod
