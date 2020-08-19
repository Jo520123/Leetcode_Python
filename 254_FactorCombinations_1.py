class Solution:
    def getFactors(self, n):
        """
               :param n: int
               :return: List[List[int]]
                """
        ans = []
        fac = []
        self.DFS(n, ans, fac)
        return ans

    def DFS(self, n, ans, fac):

        if not fac:
            x = 2
        else:
            x = fac[-1]

        while x <= n/x:
            if n % x == 0:
                fac.append(x)
                fac.append(int(n/x))
                ans.append(list(fac))
                fac.pop(-1)
                self.DFS(int(n/x), ans, fac)
                fac.pop(-1)

            x += 1
