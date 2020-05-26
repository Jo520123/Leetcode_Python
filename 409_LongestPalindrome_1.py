class Solution:
    def LongestPalindrome(self, s):
        """
               :type s: str
               :rtype: int
               """
        mapdict = dict()

        for i in s :
            if i in mapdict.keys():
                mapdict[i] +=1
            else:
                mapdict[i] = 1

        r = 0
        m = 0

        for j in mapdict.keys():
            if mapdict[j] % 2 == 1:
                m+=1
            r += mapdict[j]//2

        r = r *2 +1 if m > 0 else r*2

        return r if r > 0 else (1 if m > 0 else 0)



