class Solution:
    def spiralOrder(self, matrix):
        """
        :param matrix: List[List[int]
        :return: List[int]
        """

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []

        r, c = len(matrix), len(matrix[0])
        result = matrix[0]

        if r > 1:
            for i in range(1, r):
                result.append(matrix[i][c-1])

            for j in range(c-2, -1, -1):
                result.append(matrix[r-1][j])

            if c > 1:
                for i in range(r-2, 0, -1):
                    result.append(matrix[i][0])

        M = []
        for k in range(1, r-1):
            M.append(matrix[k][1:-1])

        return result + self.spiralOrder(M)

