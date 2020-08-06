class Solution:
    def subsets(self, nums):
        """
        :param nums: List[int]
        :return: List[List[int]]
        """
        r = []
        self.DFS(nums, r, 0, [])
        return r

    def DFS(self, nums, r, idx, route):
        r.append(route)
        for i in range(idx, len(nums)):
            self.DFS(nums, r , i+1 , route + [nums[i]])
