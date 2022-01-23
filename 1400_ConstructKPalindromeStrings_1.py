from collections import Counter

class Solution:
    def canConstruct(self, s, k):
        """
        :param s: str
        :param k: int
        :return: bool
        """

        if len(s) < k:
            return False

        oddNumber = 0

        element = Counter(s)

        for i,j in element.items():

            if j % 2 != 0:
                oddNumber += 1


        if oddNumber > k:
            return False


        return True
