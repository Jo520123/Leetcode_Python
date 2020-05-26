class Solution:
    def RemoveDuplicates(nums):
        """
                :type nums: List[int]
                :rtype: int
            """
        len= 1
        if len(nums)==0:
            return 0
        for i in range (1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[len] = nums[i]
                len+=1
        del nums[len:len(nums)]
        return len

