class Solution:
    def IsPowerOfThree(self,x):
        """
        :param x: int
        :return:bool
        """
        if x <= 0:
            return False
        while x%3 == 0:
            x/=3
        return x == 1

