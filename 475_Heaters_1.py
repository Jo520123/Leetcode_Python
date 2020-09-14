class Solution:
    def findRadius(self, houses, heaters):
        """
        :param houses:  List[int]
        :param heaters:  List[int]
        :return: int
        """
        houses.sort()
        heaters.sort()
        r = 0
        i = 0

        for h in houses:
            while i < len(heaters) and heaters[i] < h:
                i += 1
            if i == 0 :
                r = max(r, heaters[i]-h)
            elif i == len(heaters):
                r = max(r, houses[-1] - heaters[-1])
            else:
                r = max(r, min(heaters[i] - h, h - heaters[i-1]))
        return r
