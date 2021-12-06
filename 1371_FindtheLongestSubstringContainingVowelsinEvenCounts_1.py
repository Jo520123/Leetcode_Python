class Solution:
    def findTheLongestSubstring(self, s):
        """
        :param s:  str
        :return: int
        """
        dic = {0:-1}
        v = {'a' : 1, 'e' : 2, 'i' : 4, 'o' : 8, 'u': 16}
        ans, x1 = 0, 0

        for i, j in enumerate(s):

            if j in v:
                x1 ^= v[j]

            if x1 not in dic:
                dic[x1] = i

            else:
                ans = max(ans, i-dic[x1])

        return ans