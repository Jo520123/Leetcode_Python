class Solution:
    def minSteps(self, s, t):
        """
        :param s: str
        :param t: str
        :return: int
        """

        for x in s:
            t = t.replace(x,"", 1)

        return len(t)
