class Solution:
    def LengthOfLsatWord(s):
        """
            :type s: str
            :rtype: int
            """
        l, i = 0, len(s)-1
        while i>=0:
            if s[i]!=' ':
                break
            i = i-1
        for j in range(i,-1,-1):
            if s[j] == ' ':
                return l
            l = l+1
        return l

