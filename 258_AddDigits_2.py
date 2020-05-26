class Solution:
    def AddDigits(self,num):
        """
        :param num: int
        :return: int
        """
        if num ==0:
            return 0
        else:
            return 1 + (num-1) % 9

