class Solution:
    def convert(self, s, numRows):
        """
        :param s: str
        :param numRows: int
        :return: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        Zagzig = ['' for i in range(numRows)]

        row, step_diff = 0, 1

        for Chr in s:
            Zagzig[row] += Chr

            if row == 0:
                step_diff = 1
            elif row == numRows-1:
                step_diff = -1

            row += step_diff

        return ''.join(Zagzig)

