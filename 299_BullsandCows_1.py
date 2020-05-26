import collections
class Solution:
    def GetHint(self, secret, guess):
        """
              :type secret: str
              :type guess: str
              :rtype: str
              """
        b = 0
        c = 0
        secret_dict = collections.defaultdict(int)
        for s ,g in zip(secret, guess):
            if s == g:
                b+=1
            else:
                secret_dict[s] +=1
        for i,g in enumerate(guess):
            if secret[i] != guess[i] and secret_dict[g]:
                c += 1
                secret_dict[g] -= 1
        return str(b)+ 'A' + str(c) +'B'
