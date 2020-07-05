class Solution:
    def setZeroes(self, matrix):
        """
        :param matrix: List[List[int]]
        :return: None
        Do not return anything, modify matrix in-place instead
        """
        r, c = len(matrix), len(matrix[0])
        zr, zc = False, False

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
                    zr = True if i == 0 else zr
                    zc = True if j == 0 else zc


        for i in range(1,r):
            if matrix[i][0] == 0:
                for j in range(1,c):
                    matrix[i][j] = 0

        for j in range(1, c):
            if matrix[0][j] == 0:
                for i in range(1, r):
                    matrix[i][j] = 0

        if  zr:
            for j in range(c):
                matrix[0][j] = 0


        if zc:
            for i in range(r):
                matrix[i][0] = 0


        return
