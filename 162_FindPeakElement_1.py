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


x = Solution()
nums = [1,2,3,1] #2
nums1 = [1,2,1,3,5,6,4] #1 or 5
nums2 = [1] #0

print(x.findPeakElement(nums))
print(x.findPeakElement(nums1))
print(x.findPeakElement(nums2))


"""
a =[1]
ss=len(a)
b =[0,ss-1][a[0] < a[ss-1]]

print(b)
print(type(b))
"""

