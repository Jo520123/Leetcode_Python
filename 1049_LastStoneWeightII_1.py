import heapq
class Solution:
    def lastStoneWeightII(self, stones):
        """
        :param stones: List[int]
        :return: int
        """
        rev = list(map(lambda x :-x, stones))
        heapq.heapify(rev)

        while len(rev) > 1:
            first = heapq.heappop(rev)

            if rev:
                second = heapq.heappop(rev)

                if first != second:
                    heapq.heappush(rev, -abs(first-second))


        if not rev:
            return 0
        else:
            return -rev[0]
