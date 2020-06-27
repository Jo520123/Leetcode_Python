class Solution:
    def lenLongestFibSubseq(self, A):
        """
        :param A: List[int]
        :return: int
        """
        set_a = set(A)
        l = len(A)
        result = 0

        for i in range(0, l-1):
            for j in range(i+1,l):
                x, y = A[i], A[j]
                c = 2
                while x+y in set_a:
                    x, y = y, x+y
                    c +=1
                    result = max(result, c)

        if result > 2:
            return result
        else:
            return 0
