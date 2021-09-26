class Solution:
    def longestSubsequence(self, arr, difference):
        """
        :param arr: List[int]
        :param difference: int
        :return: int
        """
        d = {}
        ans = 1

        for x in arr:

            if x - difference in d:
                d[x] = d[x-difference] + 1

            else:
                d[x] = 1

            ans = max(d[x], ans)


        return ans
