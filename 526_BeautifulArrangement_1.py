class Solution:
    def countArrangement(self, N) :
        """
        :param N: int
        :return: int
        """
        self.count = 0
        v = [0] * (N+1)
        self.DFS(N, 1, v)

        return self.count



    def DFS(self, N, loct, v):
        if loct > N:
            self.count += 1
            return

        for i in range(1, N+1):
            if (i % loct == 0 or loct % i == 0) and v[i] == 0:
                v[i] = 1
                self.DFS(N, loct + 1, v)
                v[i] = 0
