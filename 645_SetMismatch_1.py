class Solution:
    def findErrorNums(self, nums):
        """
        :param nums: List[int]
        :return: List[int]
        """
        uni = set(nums)
        l = len(nums)

        lost = (l*(l+1))//2 - sum(uni)
        dupl = sum(nums) - sum(uni)

        return [dupl, lost]
