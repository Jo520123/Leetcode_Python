class Solution:
    def FirstUniquChar(self,s):
        """
                :type s: str
                :rtype: int
                """
        letter= {}
        for c in s:
            if c in letter:
                letter[c] = letter[c] + 1
            else:
                letter[c] = 1

        for i in range(len(s)):
            if letter[s[i]] == 1:
                return i

        return -1
