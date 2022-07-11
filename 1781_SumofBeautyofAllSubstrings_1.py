class Solution:
    def beautySum(self, s):
        """
        :param s:  str
        :return: int
        """
        ans = 0
        l = len(s)

        for i in range(l):

            listD = [0] * 26

            for j in range(i,l):

                listD[ord(s[j])-ord('a')] += 1

                minlistD = min(x for x in listD if x)

                ans += max(listD) - minlistD


        return ans
