class Solution:
    def IsPowerOfFour(self,num):
        """
        :param num: int
        :return: bool
        """
        if num <=0:
            return False
        if num == 1:
            return True
        if num % 4 == 0:
            return self.IsPowerOfFour(num / 4)
        return False
