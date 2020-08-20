class Solution:
    def canWin(self, s):
        """
        :param s: str
        :return: bool
        """
        idx = len(s) - 1

        for i in range(idx):
            if s[i:i+2] == '++':
                first = s[:i] + '--' + s[i+2:]

                if not self.canWin(first):
                    return True

        return False
