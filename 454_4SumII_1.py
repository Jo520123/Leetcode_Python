class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :param A: List[int]
        :param B: List[int]
        :param C: List[int]
        :param D: List[int]
        :return: int
        """
        table = dict()
        ans = 0

        for x in A:
            for y in B:
                if (x+y) not in table:
                    table[(x+y)] = 1
                else:
                    table[(x+y)] += 1

        for z in C:
            for w in D:
                if -(z+w) in table:
                    ans += table[-(z+w)]

        return ans
