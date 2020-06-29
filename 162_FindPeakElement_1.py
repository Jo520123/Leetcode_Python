class Solution:
    def findPeakElement(self, nums):
        """
        :param nums: List[int]
        :return: int
        """
        for i in range(1,len(nums)-1):
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i

        return [0, len(nums)-1][nums[0] < nums[len(nums)-1]]

