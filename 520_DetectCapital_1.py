class Solution:
    def detectCapitalUse(self, word):
        """
        :param word:  str
        :return: bool
        """
        c = 0
        for x in word:
            if x.isupper():
                c += 1
        if c == len(word):
            return True
        elif c == 0:
            return True
        elif c == 1 and word[0].isupper():
            return True
        else:
            return False
