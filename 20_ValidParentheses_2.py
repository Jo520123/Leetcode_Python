class Solution:
    def IsValid(s):
        """
        type s: str
        :rtype: bool
        """
        brackets = ["()", "[]", "{}"]
        while any(i in s for i in brackets):
            for bracket in brackets:
                s = s.replace(bracket,'')
        return not s

