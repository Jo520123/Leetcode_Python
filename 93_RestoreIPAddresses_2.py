class Solution:
    def restoreIpAddresses(self, s):
        """
        :param s:  str
        :return: List[str]
        """

        result = []
        self.DFS(s, [], result)
        return result

    def DFS(self, s, route ,result):
        if len(s) > 3*(4-len(route)):
            return

        if len(route) == 4 and not s:
            result.append('.'.join(route))
            return

        digit = min(3,len(s))

        for i in range(digit):
            n = s[:i+1]
            if int(n) > 255 or (len(n) >= 2 and n[0] == '0'):
               continue
            self.DFS(s[i+1:], route + [s[:i+1]], result)
