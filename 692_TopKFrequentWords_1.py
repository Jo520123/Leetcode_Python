from collections import Counter
from heapq import heappushpop
from heapq import heapify
import heapq
class Solution:
    def topKFrequent(self, words, k):
        """
        :param words: List[str]
        :param k: int
        :return: List[str]
        """
        ans = []
        if len(words) == 0:
            return ans

        table = Counter(words)
        big_stack = [(-j,i) for i,j in table.items()]

        heapq.heapify(big_stack)

        for i in range(k):

            ans.append(heapq.heappop(big_stack)[1])

        return ans
