from collections import Counter
class Solution:
    def leastBricks(self, wall):
        """
        :param wall: List[List[int]]
        :return: int
        """

        l_side = Counter()
        c = 0

        for x in wall:
            r_sum = 0

            for i in range(len(x)-1):
                r_sum += x[i]
                l_side.update([r_sum])
                c = max(l_side[r_sum], c)


        return len(wall) - c
