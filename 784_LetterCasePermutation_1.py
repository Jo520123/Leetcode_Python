class Solution:
    def letterCasePermutation(self, S ):
        """
        :param S: str
        :return: List[str]
        """
        result = []
        self.DFS(S, result, "", 0)
        return result


    def DFS(self, S, result, route, idx):
        if len(S) == idx:
            result.append(route)
            return

        else:
            if S[idx].isalpha():
                self.DFS( S, result, route + S[idx].lower(), idx+1)
                self.DFS( S, result, route + S[idx].upper() , idx+1)
            else:
                self.DFS( S, result, route + S[idx] , idx+1)
