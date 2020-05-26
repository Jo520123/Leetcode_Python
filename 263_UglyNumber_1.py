class Solution:
    def IsUgly(self,num):
        """
        :param num: int
        :return: bool
        """
        if num <= 0:
            return False

        for i in [2,3,5]:
            while num % i == 0:
                num = num /i
        return True if num == 1 else False
