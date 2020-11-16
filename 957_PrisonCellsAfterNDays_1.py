from copy import deepcopy
class Solution:
    def prisonAfterNDays(self, cells, N):
        """
        :param cells: List[int]
        :param N: int
        :return: List[int]
        """

        l = len(cells)
        c = 0

        cyc = N % 14
        if cyc == 0:
            cyc = 14

        while c < cyc:
            ncells = [0] * 8

            for i in range(1,l-1):
                if cells[i-1] == cells[i+1]:
                    ncells[i] = 1
                else:
                    ncells[i] = 0

            cells = ncells
            c += 1

        return cells
