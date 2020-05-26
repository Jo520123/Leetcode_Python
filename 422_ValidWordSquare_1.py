class Solution:
    def ValidWordSquare(self, words):
        """
               :type words: List[str]
               :rtype: bool
               """
        x = len(words)
        for i in range(x):
            m = len(words[i])
            for j in range(m):
                try:
                    if words[i][j] != words[j][i]:
                        return False
                except:
                    return False

        return True

