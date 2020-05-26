class Solution:
    def searchInsert(nums, target):
        """
                :type nums: List[int]
                :type target:int
                :rtype: int
                """
        try:
            return nums.index(target)
        except:
            if nums[-1] - target < 0:
                return (nums.index(nums[-1]) + 1)

            for i in range (len(nums)):
                if nums[i]-target > 0:
                    return i


