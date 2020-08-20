class Solution:
    def nextPermutation(self, nums):
        """
        :param nums: List[int]
        :return: None
        """
        l = len(nums) - 1

        while l > 0 and nums[l] <= nums[l-1]:
            l -= 1

        self.inverse(nums, l, len(nums)-1)


        if l > 0:
            for i in range(l, len(nums)):
                if nums[i] > nums[l-1]:
                    nums[l-1],nums[i] = nums[i], nums[l-1]
                    break


    def inverse(self, nums, x, y):
        summ = int((x+y)/2)
        for v in range(x, summ + 1):
            nums[v], nums[x+y-v] = nums[x+y-v], nums[v]
