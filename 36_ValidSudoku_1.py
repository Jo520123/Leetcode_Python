class Solution:
    def isValidSudoku(self, board):
        """
        :param board: List[List[str]]
        :return: bool
        """
        return self.isRowValid(board) and self.isColValid(board) and self.isSquareValid(board)


    def isRowValid(self,board):
        for r in board:
            if not self.isUnitValid(r):
                return False
        return True

    def isColValid(self, board):
        for c in zip(*board):
            if not self.isUnitValid(c):
                return False
        return True

    def isSquareValid(self, board):
        for i in (0,3,6):
            for j in (0,3,6):
                s = [board[row][col] for row in range(i, i+3) for col in range(j, j+3)]
                if not self.isUnitValid(s):
                    return False
        return True


    def isUnitValid(self, u):
        u = [i for i in u if i != "."]
        return len(set(u)) == len(u)
