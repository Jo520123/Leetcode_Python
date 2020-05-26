class NumArray:

    def __init__(self, nums):
        """
         :type nums: List[int]
         """
        N = len(nums)
        self.sums = [0] * (N+1)
        for i in range(1, N+1):
            self.sums[i] = self.sums[i-1] + nums[i-1]


    def sumRange(self, i, j):
        """
         :type nums: List[int]
         """
        return self.sums[j+1] - self.sums[i]

