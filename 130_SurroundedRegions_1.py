class Solution:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        :param board:List[List[str]]
        :return: None
        """
        if not board:
            return board

        ewsn = [ (1,0), (-1,0), (0,-1), (0,1)]
        r, c = len(board), len(board[0])
        check = set()

        def DFS(i,j):
            for x, y in ewsn:
                ni,nj = i + x, j + y
                if 0 <= ni< r and 0 <= nj< c and board[ni][nj] == 'O' and (ni,nj) not in check:
                    board[ni][nj] = '#'
                    check.add((ni, nj))
                    DFS(ni, nj)

        for i in range(r):
            for j in range(c):
                if (i == 0 or i == r-1 or j == 0 or j == c-1) and board[i][j] == 'O' and (i,j) not in check:
                    check.add((i, j))
                    board[i][j] = '#'
                    DFS(i,j)

        for i in range(r):
            for j in range(c):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

                elif board[i][j] == '#':
                    board[i][j] = 'O'
