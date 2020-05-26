class Solution(object):
    def ReverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        for i in range(0, len(s)//2):
            tmp = s[i]
            s[i] = s[len(s)-1-i]
            s[len(s)-1-i] =tmp

        return ''.join(s)
