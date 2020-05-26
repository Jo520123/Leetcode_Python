class Solution:
    def Rob(self, nums):
        """
           :type nums: List[int]
           :rtype: int
           """
        cur = last = 0
        for i in nums:
            last, cur = cur, max(i+last, cur)
        return cur
