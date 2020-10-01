from collections import Counter
class Solution:
    def topKFrequent(self, nums, k):
        """
        :param nums: List[int]
        :param k: int
        :return: List[int]
        """
        ans = []
        c = Counter(nums).most_common()

        for i in range(k):
            ans.append(c[i][0])

        return ans
