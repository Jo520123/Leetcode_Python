class Solution:
    def permuteUnique(self, nums):
        """
        :param nums: List[int]
        :return: List[List[int]]
        """

        result = []
        self.DFS(nums, result, [])

        return result


    def DFS(self, n, result, route):
        if route not in result and not n:
            result.append(route)

        else:
            for i in range(len(n)):
                self.DFS(n[:i]+n[i+1:], result, route + [n[i]])
