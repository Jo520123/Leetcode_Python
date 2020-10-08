class Solution:
    def islandPerimeter(self, grid):
        """
        :param grid:  List[List[int]]
        :return: int
        """
        row, col = len(grid), len(grid[0])

        island = 0
        near = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    island += 1

                    if j < col -1:
                        if grid[i][j+1] == 1:
                            near += 1

                    if i < row - 1:
                        if grid[i+1][j] == 1:
                            near += 1

        return (island*4) - (near*2)
