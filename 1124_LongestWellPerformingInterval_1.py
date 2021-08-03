class Solution:
    def longestWPI(self, hours):
        """
        :param hours:List[int]
        :return: int
        """

        c = 0
        d = {}
        ans = 0
        l = len(hours)

        for i in range(l-1):
            if hours[i] > 8:
                c += 1
            else:
                c -= 1

            if c not in d:
                d[c] = i

            if c-1 in d:
                ans = max(i-d[c-1], ans)

            if c == 1:
                ans = max( i+1,ans)

        cc = 0

        for i in range(l-1, -1,-1):
            if hours[i] > 8:
                cc += 1
            else:
                cc -= 1

            if cc > 0:
                ans = max(l-i,ans)


        return ans
