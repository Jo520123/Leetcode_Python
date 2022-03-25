class Solution:
    def hasAllCodes(self, s, k):
        """
        :param s: str
        :param k: int
        :return: bool
        """

        uni = set()
        c = 1 << k

        for i in range(len(s)-k , -1, -1):
            window = s[i:i+k]

            if window not in uni:
                uni.add(window)
                c -= 1

            if c == 0:
                return True

            if i < c:
                return False
