class Solution:
    def replaceWords(self, dictionary, sentence):
        """
        :param dictionary:  List[str]
        :param sentence: str
        :return: str
        """
        self.dict1 = set(dictionary)
        sep = sentence.split()
        recombine = map(self.substitute, sep)
        ans = ' '.join(recombine)

        return ans


    def substitute(self, sep):
        for i in range(len(sep)):
            if sep[:i] in self.dict1:
                return sep[:i]

        return sep

