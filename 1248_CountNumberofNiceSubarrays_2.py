class Solution:
    def numberOfSubarrays(self, nums, k):
        """
        :param nums: List[int]
        :param k: int
        :return: int
        """
        clist = []
        c = 0
        ans = 0

        for x in nums:
            if x % 2 == 0:
                c += 1

            else:
                clist.append(c)
                c = 0

        clist.append(c)

        for i in range(len(clist)-k):

            ans += (1+clist[i]) * (1+clist[i+k])

        return ans

