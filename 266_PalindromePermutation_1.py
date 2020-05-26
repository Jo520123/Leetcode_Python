from collections import Counter
class Solution:
    def CanPermutePalinddrome(self,s):
        """
               :type s: str
               :rtype: bool
               """
        c = Counter(s)
        chance = 1
        for char in c:
            if c[char] % 2 != 0:
                chance -=1
                if chance < 0:
                    return False
        return True

