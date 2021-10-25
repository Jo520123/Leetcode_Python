from collections import Counter
class Solution:
    def minSteps(self, s, t):
        """
        :param s: str
        :param t: str
        :return: int
        """
        cs = Counter(s)
        ct = Counter(t)
        ans = 0

        for x in cs.keys():
            if x not in ct:
                ans += cs[x]

            elif x in ct and cs[x] > ct[x]:
                ans += cs[x] -ct[x]

        return ans
