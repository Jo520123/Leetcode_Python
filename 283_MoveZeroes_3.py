class Solution(object):
    def MoveZeroes(self, nums):
        """
            :type nums: List[int]
            :rtype: void
            """
        i = 0
        for num in nums:
            if num !=0:
                nums[i] = num
                i +=1
        for j in range(i, len(nums)):
            nums[j] =0
        
        return nums






