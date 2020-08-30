class Solution:
    def assignBikes(self, workers, bikes):
        """
        :param workers: List[List[int]]
         :param  bikes: List[List[int]]
        :return: int
        """
        row, col = len(workers), len(bikes)

        matrix = [[i for i in range(row)] for j in range(col)]

        visit = {}
        ubike = set()

        for i, j in enumerate(workers):
            w_i, w_j = j[0], j[1]

            for ii, jj in enumerate(bikes):
                b_i, b_j = jj[0], jj[1]
                matrix[i][ii] = abs(w_i - b_i) + abs(w_j - b_j)

        return self.DFS(0, ubike, visit, row, col, matrix)


    def DFS(self, row_start, ubike, visit, row, col, matrix):
        if row_start >= row:
            return 0

        status = (row_start, tuple(ubike))

        if status in visit:
            return visit[status]

        else:
            val = float('inf')

            for i in range(col):
                if i not in ubike:
                    ubike.add(i)
                    sum = matrix[row_start][i] + self.DFS(row_start + 1, ubike, visit, row, col, matrix)
                    ubike.remove(i)
                    val = min(val, sum)

            visit[status] = val

            return val
