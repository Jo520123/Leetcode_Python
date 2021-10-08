class Solution:
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        """
        :param s: str
        :param maxLetters: int
        :param minSize: int
        :param maxSize: int
        :return: int
        """

        l, d, uni, ans = len(s), dict(), set(), 0

        for i in range(l-minSize+1):
            subl = minSize

            while subl <= maxSize and i+subl <= l :
                win = s[i:i+subl]

                for x in win:
                    if len(uni) > maxLetters:
                        break
                    uni.add(x)

                if len(uni) <= maxLetters:
                    d[win] = d.get(win,0) + 1

                    ans = max(d[win],ans)

                uni.clear()

                subl += 1

        return ans
