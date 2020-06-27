class Solution:
    def reverseWords(self, s):
        """
        :param s: str
        :return: str
        """
        if s == "":
            return s

        sep_s = s.split()

        if sep_s == []:
            return ""

        result = ""
        for i in range(0,len(sep_s)-1):
            result += sep_s[len(sep_s)-1-i] + " "
        result += sep_s[0]

        return result
