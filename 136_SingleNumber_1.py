class Solution:
    def SingleNumber(self, nums):
        """
        :type nums: List [int]
        :rtype: int
        """
        no_duplicatelist = []
        for i in nums:
            if i not in no_duplicatelist:
                no_duplicatelist.append(i)
            else:
                no_duplicatelist.remove(i)
        return no_duplicatelist.pop()
