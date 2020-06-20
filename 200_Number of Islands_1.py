class Solution:
    def numIslands(self, grid):
        """
        :param grid: List[List[str]]
        :return: int
        """
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    self.dfs(grid, row, col)
                    count += 1

        return count


    def dfs(self, grid, r, c):
        ewsn = [[-1,0], [1,0], [0,1], [0,-1]]
        grid[r][c] = "0"
        for x in ewsn:
            new_row, new_col = r + x[0], c + x[1]
            if new_row >= 0 and new_col >= 0 and new_row < len(grid) and new_col < len(grid[0]):
                if grid[new_row][new_col] == "1":
                    self.dfs(grid, new_row, new_col)
