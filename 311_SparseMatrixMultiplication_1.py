class Solution():
    def multiply(self, A, B):
        """
        :param A: List[List[int]]
        :param B: List[List[int]]
        :return: List[List[int]]
        """
        if len(A) == 0 and len(B) == 0:
            return [[]]

        row_a, row_b, col_b = len(A), len(B), len(B[0])
        A_mul_B = [[0 for i in range(col_b)] for i in range(row_a)]

        for i in range(row_a):
            for j in range(row_b):
                if A[i][j] != 0:
                    for k in range(col_b):
                        if B[j][k] != 0:
                            A_mul_B[i][k] = A[i][j] * B[j][k]

        return A_mul_B



