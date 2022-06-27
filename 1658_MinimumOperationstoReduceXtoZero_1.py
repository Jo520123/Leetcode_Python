class Solution:
    def minOperations(self, nums, x):
        """
        :param nums: List[int]
        :param x: int
        :return: int
        """

        total = 0
        n = len(nums)
        l = 0
        goal = sum(nums) - x
        mlen = 0
        flag = False

        for i in range(n):
            total += nums[i]

            while l < i and total > goal:
                total -= nums[l]
                l += 1


            if total == goal:
                flag = True
                mlen = max(i-l+1, mlen)


        if flag == True:

            return len(nums) - mlen

        else:
            return -1
