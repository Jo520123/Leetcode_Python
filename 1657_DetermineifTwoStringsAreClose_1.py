from collections import Counter
class Solution:
    def closeStrings(self, word1, word2):
        """
        :param word1: str
        :param word2: str
        :return: bool
        """

        d1 = Counter(word1)
        d2 = Counter(word2)

        for x, y in d1.items():
            if x not in d2:
                return False

        sd1 = sorted(d1.values())
        sd2 = sorted(d2.values())

        for x, y in zip(sd1, sd2):

            if x != y :
                return False

        return True
