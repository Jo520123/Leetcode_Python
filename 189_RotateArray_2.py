class Solution:
    def Rotate(self, nums, m):
        n = len(nums)
        b = [0] * n
        for i in range(n):
            b[(i+m) % n]= nums[i]

        nums[:] = b
        return nums
