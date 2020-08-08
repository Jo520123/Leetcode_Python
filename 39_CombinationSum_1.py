class Solution:
    def combinationSum(self, candidates, target):
        """
        :param candidates: List[int]
        :param target: int
        :return:  List[List[int]]
        """

        result = []
        candidates = sorted(candidates)
        self.DFS(candidates, target,  [], result, 0 )

        return result


    def DFS(self, candidates, target, route, result, idx ):

        for i in range(idx, len(candidates)):
            ans = target - candidates[i]

            if ans < 0:
                break

            if ans == 0:
                result.append(route + [candidates[i]])
                break

            self.DFS(candidates, ans, route+[candidates[i]], result, i)
