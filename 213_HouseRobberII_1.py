class Solution:
    def rob(self, nums):
        """
        :param nums:  List[int]
        :return: int
        """
        if not nums:
            return 0
        elif len(nums) < 3:
            return max(nums)
        else:
            return max(self.rob_without_fl(nums[1:]),self.rob_without_fl(nums[:-1]))

    def rob_without_fl(self,nums):
        m = [0] * len(nums)
        m[0], m[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            m[i] = max(nums[i] + m[i-2], m[i-1])
        return m[len(nums)-1]
