class Solution:
    def subarraySum(self, nums , k):
        """
        :param nums: List[int]
        :param k: int
        :return: int
        """
        s, c = 0, 0
        total ={}

        for i in range(len(nums)):
            s += nums[i]

            if s == k:
                c += 1

            if s-k in total:
                c += total[s-k]

            if s in total:
                total[s] += 1

            else:
                total[s] = 1

        return c
