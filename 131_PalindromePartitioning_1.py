class Solution:
    def partition(self, s) :
        """
        :param s: str
        :return: List[List[str]]
        """
        result = []
        self.DFS(s,[], result)
        return result


    def isPaindrome(self, s):
        w = ''.join(reversed(s))
        if s == w:
            return True
        return False


    def DFS(self, s, route, result):
        if not s:
            result.append(route)
            return

        for i in range(0, len(s)):
            if self.isPaindrome(s[:i+1]):
                self.DFS(s[i+1:], route +[s[:i+1]], result)
