from collections import Counter

class Solution:
    def findAnagrams(self, s, p):
        """
        :param s: str
        :param p: str
        :return: List[int]
        """
        ls = len(s)
        lp = len(p)

        result = []

        if ls < lp:
            return result

        cs = Counter(s[:lp-1])
        cp = Counter(p)

        for i in range(lp-1, ls):
            cs[s[i]] += 1

            if cs == cp:
                result.append(i -lp +1)

            cs[s[i-lp+1]] -= 1

            if  cs[s[i-lp+1]] == 0:
                del cs[s[i-lp+1]]

        return result
