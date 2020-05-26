class Solution:
    def StrStr(haystack, needle):
        """
        haystack: str
        :param needle:str
        :return: int
        """
        if (needle == ""):
            return 0
        if (needle in haystack):
            return haystack.index(needle)
        else:
            return -1


