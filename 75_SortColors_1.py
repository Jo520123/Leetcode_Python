class Solution:
    def sortColors(self, nums):
        """
         Do not return anything, modify nums in-place instead.
        :param nums: List[int]
        :return: None
        """
        i ,j = 0, 0
        k = len(nums)-1

        while j <= k:
            if i < j and nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            elif nums[j] == 2:
                nums[k], nums[j] = nums[j], nums[k]
                k -= 1
            else:
                j += 1

        return nums

