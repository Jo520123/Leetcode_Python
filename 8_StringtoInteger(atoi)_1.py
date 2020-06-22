import re
class Solution:
    def myAtoi(self, str):
        """
        :param str: str
        :return: int
        """
        strip_str = str.strip()

        if strip_str == "" or strip_str == "-" or strip_str == "+":
            return 0

        s = re.match('[^\d]+', (strip_str.lstrip("-")).lstrip("+"))

        if s != None:
            return 0

        else:
            s = re.search('\-*\+*\d+', strip_str).group()

        if s[0:2] == "--" or s[0:2] == "-+" or s[0:2] == "++":
            return 0

        result = int(s)

        if result > 0:
            if result > 2147483647:
                return 2147483647
            else:
                return result
        else:
            if result < -2147483648:
                return -2147483648
            else:
                return result
