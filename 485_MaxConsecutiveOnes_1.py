class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :param nums: List[int]
        :return: int
        """
        c, r = 0, 0

        for n in nums:
            if n == 1:
                c += 1
            else:
                r = max(r, c)
                c = 0
        return max(c,r)

