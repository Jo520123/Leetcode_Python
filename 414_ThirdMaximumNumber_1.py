class Solution:
    def ThirdMax(self, nums):
        nums = sorted(list(set(nums)))
        if len(nums) < 3:
            return max(nums)
        else:
            return nums[-3]
