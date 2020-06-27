class Solution:
    def permute(self, nums):
        """
        :param nums:  List[int]
        :return: List[List[int]]
        """
        if len(nums) <= 1:
            return [nums]

        result = []
        for i , num in enumerate(nums):
            x = nums[:i] + nums[i+1:]
            for j in self.permute(x):
                result.append([num] + j)

        return result
