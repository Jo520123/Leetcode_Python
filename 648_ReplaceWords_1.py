class Solution:
    def replaceWords(self, dictionary, sentence):
        """
        :param dictionary:  List[str]
        :param sentence: str
        :return: str
        """

        sep = sentence.split()

        for i in range(len(sep)):
            for x in dictionary:
                if sep[i].startswith(x):
                    sep[i] = x


        ans = ' '.join(sep)

        return ans
