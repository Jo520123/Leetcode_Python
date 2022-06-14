class Solution:
    def maxNonOverlapping(self, nums, target):
        """
        :param nums: List[int]
        :param target: int
        :return: int
        """
        c = 0
        d = {0:1}
        sum = 0

        for x in nums:
            sum += x
            remaining = sum -target


            if remaining in d:

                d = {0:1}
                c += 1
                sum = 0

            else:

                d[sum] = 1

        return c
