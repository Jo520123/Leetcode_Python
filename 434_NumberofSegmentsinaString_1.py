class Solution:
    def CountSegments(self,s):
        """
                :type s: str
                :rtype: int
                """
        if s.isspace():
            return 0
        ss = s.strip()
        if len(ss) == 0:
            return 0
        a = [0]
        m = list(ss)
        while m:
            if m[0] != ' ':
                a[-1]+=1
            else:
                a.append(0)
            m.pop(0)
        return len(a) - a.count(0)

