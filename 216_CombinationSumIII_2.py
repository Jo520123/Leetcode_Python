class Solution:
    def combinationSum3(self, k , n):
        """
        :param k: int
        :param n: int
        :return: List[List[int]]
        """
        result = []
        all_num = [i for i in range(1, 10)]
        self.DFS(all_num, k, n, result, [], 0)
        return result

    def DFS(self, all_num, k, n, result, route, idx):
        if k < 0 or n < 0:
            return

        elif k == 0 and n == 0:
            result.append(route)
            return

        for i in range(idx, len(all_num)):
            self.DFS(all_num, k - 1, n - all_num[i], result, route + [all_num[i]], i + 1)
