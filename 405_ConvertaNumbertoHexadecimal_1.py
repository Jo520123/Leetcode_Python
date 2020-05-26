class Solution:
    def ToHex(self, num):
        """
                :type num: int
                :rtype: str
                """
        a = []
        hexs = '0123456789abcdef'
        if num < 0: num += 0x100000000
        while num:
            a.append(hexs[num % 16])
            num //= 16
        return ''.join(a[::-1]) if a else '0'
