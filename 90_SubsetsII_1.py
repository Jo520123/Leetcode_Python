class Solution:
    def subsetsWithDup(self, nums):
        """
        :param nums: List[int]
        :return: List[List[int]]
        """
        result = []
        ns = sorted(nums)
        self.DFS(ns , 0, [], result)

        return result

    def DFS(self, ns, idx, route, result):
        result.append(route)
        for i in range(idx, len(ns)):
            if i > idx and ns[i] == ns[i-1]:
                continue

            self.DFS(ns, i+1, route+[ns[i]], result)
