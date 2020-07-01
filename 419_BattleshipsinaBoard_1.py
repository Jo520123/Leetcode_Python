class Solution:
    def countBattleships(self, board):
        """
        :param board:  List[List[str]]
        :return: int
        """

        def valid(r, c):
            if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]):
                return False
            else:
                return True

        def dfs(r,c):
            if not valid(r,c):
                return
            if board[r][c] == ".":
                return
            board[r][c] = "."
            dfs(r, c+1)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r-1, c)

        if not board:
            return

        ship_count= 0
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "X":
                    ship_count += 1
                    dfs(r,c)

        return ship_count
