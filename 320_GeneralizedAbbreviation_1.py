class Solution:
    def generateAbbreviations(self, word):
        """
        :param word: str
        :return: List[str]
        """
        result = []
        self.DFS(word, result, 0, "")
        return result


    def DFS(self, word, result, idx, s):
        if len(word) == idx:
            result.append(s)
            return

        for i in range(idx, len(word)):
            if i-idx > 0:
                n = str(i - idx)
            else:
                n = ""

            self.DFS(word, result, i + 1, s + n + word[i])

        self.DFS(word, result, len(word), s + str(len(word)-idx))
