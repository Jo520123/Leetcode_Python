class Solution:
    def RemoveElement(nums, val):
        """
                :type nums: Lists[int]
                :type val: int
                :rtype: int
                """
        c = 0
        for i in range (len(nums)):
            if nums[i]!=val:
                nums[c] = nums[i]
                c+=1
        return c



