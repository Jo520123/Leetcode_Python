class Solution:
    def countNegatives(self, grid):
        """
        :param grid: List[List[int]]
        :return: int
        """
        ng = []
        for i in grid:
            i = sorted(i)
            ng.append(i)


        c = 0
        row, col = len(ng), len(ng[0])
        i, j  = 0, col-1

        while i < row and j >= 0:

            if ng[i][j] < 0:
                c += (j+1)
                i += 1
                j = col-1

            else:
                if j == 0:
                    i += 1
                    j = col-1
                else:
                    j -= 1

        return c
