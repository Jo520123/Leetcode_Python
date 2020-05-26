class Solution:
    def MaxSubArray(nums):
        """
            :type nums:  List[int]
            :rtype: int
            """
        m = n = float("-inf")
        for i in nums:
            m = max (m+i,i)
            n = max (n,m)
        return n


