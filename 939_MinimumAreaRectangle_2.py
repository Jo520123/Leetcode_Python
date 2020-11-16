from collections import defaultdict
class Solution:
    def minAreaRect(self, points):
        """
        :param points: List[List[int]]
        :return: int
        """
        points = map(tuple, points)
        xd, yd = defaultdict(list), defaultdict(list)
        ans = float("inf")
        unique_vertex = set()

        for p in points:
            xd[p[0]].append(p)
            yd[p[1]].append(p)
            unique_vertex.add(p)


        for k in xd.keys():
            if len(xd[k]) == 1:
                continue

            for i in range(len(xd[k])-1):
                vertex1 = xd[k][i]

                for j in range(i+1, len(xd[k])):
                    vertex2 = xd[k][j]

                    for vertex3 in yd[vertex1[1]]:
                        if vertex1 != vertex3:
                            if (vertex3[0], vertex2[1]) in unique_vertex:
                                ans = min(ans, abs(vertex3[0]-vertex1[0]) * abs((vertex2[1]-vertex1[1])))

        if ans != float("inf"):
            return ans

        else:
            return 0
