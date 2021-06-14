class Solution:
    def maxEqualRowsAfterFlips(self, matrix):
        """
        :param matrix: List[List[int]]
        :return: int
        """
        d = dict()

        row, col = len(matrix), len(matrix[0])
        ans = 0

        for i in range(0,row):
            r= ""
            for j in range(0, col):
                if (matrix[i][0] == 1):
                    r += str(matrix[i][j])

                else:
                    r += str(int(not(matrix[i][j])))

            if r in d:
                d[r] += 1

            else:
                d[r] = 1

            ans = max(ans,d[r])

        return ans