class Solution:
    def alphabetBoardPath(self, target):
        """
        :param target: str
        :return: str
        """
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        d ={}
        ans = ''
        x0, y0 = 0, 0

        for i in range(len(board)):
            for j in range(len(board[i])):
                d[board[i][j]]=(i,j)

        for w in target:
            x1, y1 = d[w]

            if w == 'z':

                b = y0 - y1

                if b > 0:
                    ans += b* 'L'
                else:
                    ans += (-b) * 'R'

                a = x0 - x1

                if a > 0:
                    ans += a * 'U'
                else:
                    ans += (-a) * 'D'

            else:
                a = x0 - x1
                if a > 0:
                    ans += a * 'U'
                else:
                    ans += (-a) * 'D'

                b = y0 - y1

                if b > 0:
                    ans += b * 'L'
                else:
                    ans += (-b) * 'R'

            ans += '!'
            x0,y0 = x1, y1

        return ans
