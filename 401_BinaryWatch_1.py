class Solution:
    def ReadBinaryWatch(self,num):
        """
                :type num: int
                :rtype: List[str]
                """
        a = []
        for x in range(1024):
            if bin(x).count('1') == num:
                h, m = x >> 6, x & 0x3F
                if h < 12 and m < 60:
                    a.append('%d:%02d' % (h,m))
        return a


