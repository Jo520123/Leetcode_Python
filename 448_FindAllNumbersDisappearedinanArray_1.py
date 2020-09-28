class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :param nums:  List[int]
        :return: List[int]
        """
        l = len(nums)
        x = set([i for i in range(1, l+1)])
        y = set(nums)

        return list(x-y)
