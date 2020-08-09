class Solution:
    def restoreIpAddresses(self, s):
        """
        :param s:  str
        :return: List[str]
        """
        if len(s) > 12:
            return []

        result = []
        self.DFS(s,[],result)

        return result


    def DFS(self, s, route, result):
        if len(route) == 4 and not s:
            result.append('.'.join(route))
            return

        for i in range(1,4):
            if i > len(s):
                continue

            n = int(s[:i])
            if n <= 255 and str(n)==s[:i] :
                self.DFS(s[i:], route + [s[:i]], result)
