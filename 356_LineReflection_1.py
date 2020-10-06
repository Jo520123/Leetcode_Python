class Solution:
    def isReflected(self, points):
        """
         :param  points: List[List[int]]
         :return: bool
        """
        f_elmt = [i for i, j in points]
        Max_x = max(f_elmt)
        min_x = min(f_elmt)
        sum = Max_x+ min_x

        table = {}

        for i, j in points:
            if i == sum//2:
                continue

            c_point = (i,j)
            diff_points = (sum - i, j)


            if diff_points in table:
                table[diff_points] -= 1
            else:
                table[c_point] = 1


        for x in table.values():

            if x == 1:
                return False

            return True
