class Solution:
    def isPowerOfFour(self,num):
        """
        :param num: int
        :return: bool
        """
        if num <= 0:
            return False

        if num & num-1 != 0:
            return False

        b_rev = bin(num)[::-1]
        index = b_rev.index('1')

        if index % 2 == 0:
            return True
        else:
            return False
