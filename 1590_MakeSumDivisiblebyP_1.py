class Solution:
    def minSubarray(self, nums, p):
        """
        :param nums: List[int]
        :param p: int
        :return: int
        """

        l = len(nums)
        total = sum(nums) % p
        ans = l
        now = 0
        d = {0:-1}


        if total == 0:
            return 0

        for i in range(l):
            now = (now + nums[i]) % p

            if d.get((now - total) % p) is not None:
                ans = min(ans, i - d.get((now - total) % p))


            d[now] = i


        if ans < l:
            return ans

        else:
            return -1
