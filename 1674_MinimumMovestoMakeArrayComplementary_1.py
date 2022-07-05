import math
class Solution:
    def minMoves(self, nums, limit):
        """
        :param nums: List[int]
        :param limit: int
        :return: int
        """

        l = len(nums)//2
        d = [0] * (2* (limit+1))

        for i in range (l):
            lef = nums[i]
            rig = nums[-1-i]

            d[min(lef,rig)+1] -= 1
            d[lef+rig] -= 1
            d[lef+rig+1] += 1
            d[max(lef,rig)+limit+1] += 1


        ans = curval = l * 2
        for i in range(2, 2*limit+1):
            curval += d[i]

            ans = min(curval, ans)

        return ans