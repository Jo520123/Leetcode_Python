import collections
class Solution:
    def minTime(self, n, edges, hasApple):
        """
        :param n: int
        :param edges: List[List[int]]
        :param hasApple: List[bool]
        :return: int
        """
        v = [False] * n

        d = collections.defaultdict(list)

        for i, x in enumerate(edges):
            d[x[0]].append(x[1])
            d[x[1]].append(x[0])


        def DFS(node):
            count = 0
            v[node] = True
            a = hasApple[node]


            for x in d[node]:
                if not v[x]:
                    nextA , nextCount = DFS(x)

                    a = nextA or a

                    if nextA :
                        count += nextCount + 2

            return a, count

        return DFS(0)[1]
