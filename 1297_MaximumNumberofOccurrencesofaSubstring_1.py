class Solution:
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        """
        :param s: str
        :param maxLetters: int
        :param minSize: int
        :param maxSize: int
        :return: int
        """

        d = {}
        ans = 0
        for i in range(len(s)-minSize+1):
            slic = s[i:i+minSize]

            if len(set(slic)) <= maxLetters:
                d[slic] = d.get(slic,0) + 1

                ans = max(d[slic], ans)

        return ans

