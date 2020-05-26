class Solution:
    def ConvertToTitle(self, num):
        capital = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        res = []
        while num > 0:
            res.append(capital[(num-1)%26])
            num = (num-1) //26
        res.reverse()
        return ''.join(res)

