class Solution:
    def IsIsomorphic(self, s,t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        return self.HalfIsom(s, t) and self.HalfIsom(t,s)

    def HalfIsom(self, s,t):
        look_up = {}
        for i in range(len(s)):
            if s[i] not in look_up:
                look_up[s[i]] = t[i]
            elif look_up[s[i]] != t[i]:
                return False
        return True











