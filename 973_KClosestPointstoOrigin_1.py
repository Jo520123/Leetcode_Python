import math
import heapq
class Solution:
    def kClosest(self, points , K) :
        """
        :param points: List[List[int]]
        :param K: int
        :return: List[List[int]]
        """
        d = []
        for x , y in points:
            z = math.sqrt(x**2 + y**2)
            d.append((z,[x,y]))

        heapq.heapify(d)

        return [x[1] for x in heapq.nsmallest(K, d)]
