class Solution:
    def ReverseVowels(self,s):
        """
             :type s: str
             :rtype: str
             """
        VOWELS = ('a','e','i','o','u')
        size = len(s)
        l, r = 0 ,size -1
        sk = list(s)
        while True:
            while l <size and s[l].lower() not in VOWELS:
                l += 1
            while r >= 0 and s[r].lower() not in VOWELS:
                r -= 1
            if l >= r: break
            sk[l], sk[r] = sk[r], sk[l]
            l, r = l+1, r-1
        return ''.join(sk)
