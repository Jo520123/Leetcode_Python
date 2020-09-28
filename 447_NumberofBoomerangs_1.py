class Solution:
    def numberOfBoomerangs(self, points):
        """
        :param points: List[List[int]]
        :return: int
        """

        r = 0
        for i1,j1 in points:
            dic = {}
            for i2,j2 in points:
                if i1 == i2 and j1 == j2:
                    continue
                else:
                    dx = i2 -i1
                    dy = j2 -j1
                    d = dx * dx + dy *dy
                    if d in dic:
                        r += dic[d]
                        dic[d] += 1
                    else:
                        dic[d] = 1

        return 2 * r

