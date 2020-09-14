class Solution:
    def findContentChildren(self, g, s):
        """
        :param g: List[int]
        :param s: List[int]
        :return: int
        """
        i_g, i_s = len(g)-1, len(s)-1
        c = 0
        g, s = sorted(g), sorted(s)
        while min(i_g,i_s) >= 0:
            if s[i_s] >= g[i_g]:
                c += 1
                i_s -= 1
            i_g -= 1

        return c
