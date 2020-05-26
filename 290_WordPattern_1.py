class Solution:
    def WordPattern(self, pattern, str):
        """
               :type pattern: str
               :type str: str
               :rtype: bool
               """
        str_s = str.split()
        if len(pattern) != len(str_s):
            return False

        d = dict()
        for i, p in enumerate(pattern):
            if p not in d:
                d[p] = str_s[i]
            else:
                if d[p] != str_s[i]:
                    return False

        d = dict()
        for i, p in enumerate(str_s):
            if p not in d:
                d[p] = pattern[i]
            else:
                if d[p] != pattern[i]:
                    return False


        return True
