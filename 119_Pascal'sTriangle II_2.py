class Solution(object):
    def GetRow(self,row_index):
        """
        :type row_index: int
        :rtype: List[int]
        """
        res = [1] + [0]*row_index
        for i in range(row_index):
            res[0] = 1
            for j in range(i+1, 0, -1):
                res[j] = res[j] +res[j-1]
        return res
