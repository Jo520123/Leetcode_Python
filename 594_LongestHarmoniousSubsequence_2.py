from collections import Counter
class Solution:
    def findLHS(self, nums):
        """
        :param nums: List[int]
        :return: int
        """
        c = Counter(nums)
        l = 0

        for x in c.keys():
            if x+1 in c:

                l = max(c[x]+c[x+1], l)

        return l
