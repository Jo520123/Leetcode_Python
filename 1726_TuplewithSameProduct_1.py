from collections import defaultdict

class Solution:
    def tupleSameProduct(self, nums):
        """
        :param nums:  List[int]
        :return: int
        """
        l = len(nums)
        d = defaultdict(int)
        ans = 0

        for i in range(l):
            for j in range(i+1,l):
                d[nums[i]*nums[j]] += 1


        for x, y in d.items():
            if(y>1):
                ans += int(y*(y-1)/2*8)

        return ans
