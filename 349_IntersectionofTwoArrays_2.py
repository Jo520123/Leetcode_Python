class Solution:
    def Intersection(self, n1, n2):
        """
        :type n1: List[int]
        :type n2: List[int]
        :rtype: List[int]
        """
        res = []
        for i in n1:
            if i not in res and i in n2:
                res.append(i)

        return res
