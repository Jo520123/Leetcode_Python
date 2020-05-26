class Solution(object):
    def GeneratePossibleNextMoves(self,x):
        """
              :type x: str
              :rtype: List[str]
              """
        res =[]
        i, n = 0, len(x)-1
        while i < n:
            if x[i] == '+':
                while i < n and x[i+1] == '+':
                    res.append(x[:i] + '--' + x[i+2:])
                    i +=1
            i += 1
        return res
