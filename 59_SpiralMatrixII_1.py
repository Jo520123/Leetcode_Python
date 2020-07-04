class Solution:
    def generateMatrix(self, n):
        """
        :param n: int
        :return:  List[List[int]
        """
        sq =[]
        for i in range(n):
            sq.append([0 for j in range(n)])

        r_start = 0
        c_start = 0
        r_end = n -1
        c_end = n -1
        v = 1

        while r_start <= r_end and c_start <= c_end:
            for i in range(c_start, c_end+1):
                sq[r_start][i] = v
                v += 1
            r_start += 1

            for i in range(r_start, r_end+1):
                sq[i][c_end] = v
                v += 1
            c_end -= 1

            if r_start <= r_end:
                for i in range(c_end, c_start-1, -1):
                    sq[r_end][i] = v
                    v += 1
                r_end -= 1

            if c_start <= c_end:
                for i in range(r_end, r_start-1, -1):
                    sq[i][c_start] = v
                    v += 1
                c_start += 1

        return sq
