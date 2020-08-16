class Solution:
    def combinationSum3(self, k , n):
        """
        :param k: int
        :param n: int
        :return: List[List[int]]
        """

        res = []
        self.dfs(10, k, n, 1, res, [])
        return res


    def dfs(self, nums, k, n, index, res, path):
        if k < 0 or n < 0:
            return
        elif k == 0 and n == 0:
            res.append(path)
            return
        for i in range(index, nums):
            self.dfs(nums-1, k - 1, n - i, i + 1, res, path + [i])
