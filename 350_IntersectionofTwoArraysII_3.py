class Solution:
    def Intersect(self, n1, n2):
        """
        :type n1: List[int]
        :type n2: List[int]
        :rtype: List[int]
        """
        res = []
        map = {}
        for i in n1:
            map[i] = map[i]+1 if i in map else 1
        for j in n2:
            if j in map and map[j] > 0:
                res.append(j)
                map[j] -= 1
        return res
