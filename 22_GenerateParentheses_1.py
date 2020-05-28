class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype:  str
        """
        result = ""

        for i in range(len(s)):
            len_11 = len( self.SubLongestPalindrome(s, i, i))

            if len_11 > len(result):
                result = self.SubLongestPalindrome(s, i, i)

            len_12 = len(self.SubLongestPalindrome(s, i, i+1))

            if len_12 > len(result):
                result = self.SubLongestPalindrome(s, i, i+1)

        return result

    def SubLongestPalindrome(self,s,left,right):
        while left >= 0 and right<len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]
