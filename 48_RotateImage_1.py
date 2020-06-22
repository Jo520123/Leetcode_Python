class Solution:
    def rotate(self, matrix):
        """
        :param matrix: List[List[int]]
        :return: None
        """
        l = len(matrix)
        n = l - 1

        for i in range(l//2):
            for j in range(i, n-i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[n-j][i]
                matrix[n-j][i] = matrix[n-i][n-j]
                matrix[n-i][n-j] = matrix[j][n-i]
                matrix[j][n - i] = temp

        return matrix
