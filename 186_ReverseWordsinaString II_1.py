class Solution:
    def reverseWords(self, s):
        """
        :param s: List[str]
        :return: None
        """
        b = 0
        e = len(s) - 1
        while b < e:
            s[b], s[e] = s[e], s[b]
            b += 1
            e -= 1

        i = 0
        b = 0

        while i < len(s):
            if s[i] == " " or i == len(s)-1:
                if i == len(s) - 1:
                    e = i
                else:
                    e = i - 1
                while b < e:
                    s[b], s[e] = s[e], s[b]
                    b += 1
                    e -= 1
                b = i + 1
            i += 1

        return s
