class Solution:
    def numberOfSubstrings(self, s):
        """
        :param s: str
        :return: int
        """
        p1, p2, l, ans = 0, 2, len(s), 0

        if l <= 2:
            return 0

        while p1 < l - 2:
            Scope = s[p1: p2+1]

            if 'a' in Scope and 'b' in Scope and 'c' in Scope:
                ans += l - p2
                p1 += 1

            else:
                p2 += 1

                if p2 == l:
                    break

        return ans