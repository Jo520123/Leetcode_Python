class Solution:
    def shortestDistance(self, words, x, y):
        """
                :type words: List[str]
                :type x: str
                :type y: str
                :rtype: int
                """
        X = [i for i in range(len(words)) if words[i] == x]
        Y = [i for i in range(len(words)) if words[i] == y]
        return min([abs(i-j) for i in X for j in Y ])