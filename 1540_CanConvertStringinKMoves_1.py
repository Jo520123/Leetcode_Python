from collections import defaultdict

class Solution:
    def canConvertString(self, s, t, k):
        """
        :param s: str
        :param t: str
        :param k: int
        :return: bool
        """

        d = defaultdict(int)

        if len(s) != len(t):
            return False

        l = len(s)

        for i in range(l):
            chrsV = (ord(t[i]) - ord(s[i])) % 26

            if chrsV == 0:
                continue

            if (d[chrsV] * 26 + chrsV > k):
                return False


            d[chrsV] += 1

        return True
