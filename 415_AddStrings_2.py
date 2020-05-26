class Solution:
    def AddStrings(self, n1, n2):
        """
        :type n1: str
        :type n2: str
        :rtype: str
        """
        t1 = 0
        for i in n1:
            t1 *= 10
            t1 += ord(i) - 48

        t2 = 0
        for i in n2:
            t2 *= 10
            t2 += ord(i) -48

        return str(t1 +t2)
