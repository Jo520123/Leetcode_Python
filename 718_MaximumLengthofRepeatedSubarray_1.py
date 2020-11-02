class Solution:
    def findLength(self, A, B) :
        """
        :param A: List[int]
        :param B: List[int]
        :return: int
        """
        la = len(A)
        lb = len(B)

        array_table = [[0 for i in range(la+1)] for j in range(lb +1)]
        l = 0

        for i in range(la + 1):
            for j in range(lb +1):
                if i == 0 or j == 0:
                    continue

                elif A[i-1] == B[j-1]:
                    array_table[i][j] = array_table[i-1][j-1] + 1

                    l = max(l, array_table[i][j])

        return l
