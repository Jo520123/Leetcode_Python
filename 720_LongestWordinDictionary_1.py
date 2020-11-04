class Solution:
    def longestWord(self, words):
        """
        :param words: List[str]
        :return: str
        """

        ans = ""
        unique_words = set(words)

        for x in words:
            Flag1 = True
            for i in range(1, len(x)):
                if x[:i] not in unique_words:
                    Flag1 = False
                    break

            if Flag1:
                if not ans or len(x) > len(ans):
                    ans = x

                elif len(x) == len(ans) and ans > x:

                    ans = x

        return ans
