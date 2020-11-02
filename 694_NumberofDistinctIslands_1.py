class Solution:
    def numDistinctIslands(self, grid):
        """
        :param grid:  List[List[int]]
        :return: int
        """
        row, col = len(grid), len(grid[0])

        unique_island = set()
        self.v = set()
        self.EASN = [(-1, 0), (0, 1), (1, 0), (0, -1)]



        for i in range(row):
            for j in range(col):
                if grid[i][j] and (i,j) not in self.v:
                    self.v.add((i,j))
                    unique_island.add(self.DFS(i, j, (0,0), [(0,0)], grid))

        return len(unique_island)




    def DFS(self, i, j, current_position, position_reachout, grid):


        for x, y in self.EASN:
            nx, ny = i+x, j+y
            if 0 <= nx <len(grid) and 0 <= ny <len(grid[0]) and grid[nx][ny] and (nx,ny) not in self.v:
                self.v.add((nx, ny))
                new_direction = (current_position[0] + x, current_position[1] +y)
                position_reachout.append(new_direction)
                self.DFS(nx, ny, new_direction, position_reachout,grid)

        return tuple(position_reachout)
