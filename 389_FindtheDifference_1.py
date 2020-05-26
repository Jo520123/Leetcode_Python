class Solution:
    def FindTheDifference(self, x, y):
        """
                :type x: str
                :type y: str
                :rtype: str
                """
        letter =[0]*26
        for c in x :
            letter[ord(c)-97] += 1
        for c in y:
            letter[ord(c) -97] -=1
            if letter[ord(c)-97] < 0:
                return c
