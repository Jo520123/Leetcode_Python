class Solution:
    def splitIntoFibonacci(self, S):
        """
        :param S: str
        :return: List[int]
        """
        ans = []
        self.DFS(S, ans, [])
        return ans



    def DFS(self, S, ans, route):
        if len(route) >= 3 and route[-2]+route[-3] != route[-1]:
            return False

        if len(route) >= 3 and not S:
            ans.append(route)
            return True

        for i in range(len(S)):
            seq = S[:i+1]

            if int(seq) >= 2**31 or (seq[0] == '0' and len(seq)>1):
                continue

            if self.DFS(S[i+1:], ans, route + [int(seq)]):
                return True

        return False
