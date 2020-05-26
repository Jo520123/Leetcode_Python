class Solution:
    def IsPalindrome(self, s):
        news= [i.lower() for i in s if i.isalnum()]
        return news == news[::-1]

