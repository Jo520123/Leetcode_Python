class Solution:
    def exist(self, board, word):
        """
        :param board: List[List[str]]
        :param word: str
        :return: bool
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word, 0):
                    return True
        return False

    def dfs(self, board, i, j, word, word_Idx):
        if word_Idx == len(word):
            return True

        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or word[word_Idx] != board[i][j]:
            return False

        board[i][j] = "."

        output = self.dfs(board, i+1, j, word, word_Idx+1) or self.dfs(board, i-1, j, word, word_Idx+1)\
                 or self.dfs(board, i, j+1, word, word_Idx+1) or self.dfs(board, i, j-1, word, word_Idx+1)

        board[i][j] = word[word_Idx]

        return output

