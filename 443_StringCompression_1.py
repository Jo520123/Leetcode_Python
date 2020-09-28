class Solution:
    def compress(self, chars):
        """
        :param chars:  List[str]
        :return: int
        """
        l = len(chars)
        x, c = 0, 1

        for i in range(1, l+1):
            if i < l and chars[i] == chars[i-1]:
                c += 1
            else:
                chars[x] = chars[i-1]
                x += 1
                if c > 1:
                    for i in str(c):
                        chars[x] = i
                        x += 1
                c = 1

        return x





