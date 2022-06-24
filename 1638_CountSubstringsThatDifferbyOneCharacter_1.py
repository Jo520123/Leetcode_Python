class Solution:
    def countSubstrings(self, s, t):
        """
        :param s: str
        :param t:  str
        :return: int
        """

        ls = len(s)
        lt = len(t)
        ans = 0

        for i in range(ls):
            for j in range(lt):

                notSame = 0
                quantity = min(ls-i,lt-j)

                for k in range(quantity):

                    if (s[i+k] != t[j+k]):
                        notSame += 1

                    if notSame > 1:
                        break

                    ans += notSame


        return ans
