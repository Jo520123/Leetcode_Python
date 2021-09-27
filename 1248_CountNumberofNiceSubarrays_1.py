class Solution:
    def numberOfSubarrays(self, nums, k):
        """
        :param nums: List[int]
        :param k: int
        :return: int
        """
        ans =  0
        c = 0
        d = {}
        l = len(nums)
        oddd = [0] * l

        for i in range(l):
            if nums[i] %2 == 1:
                c += 1
                oddd[i] = c

            else:
                oddd[i] = c

            d[c] = d.setdefault(c,0) + 1



        for i in range(l):
            if nums[i] % 2 == 1:
                x =  oddd[i] + k -1
            else:
                x =  oddd[i] + k

            if x in d:
                ans += d[x]


        return ans


