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
        visitEdge = {}

        d = collections.defaultdict(list)

        for i,x in enumerate(edges):

            d[x[0]].append(x[1])
            d[x[1]].append(x[0])


        def DFS(node, p):
            p.append(node)
            v[node] =True

            if hasApple[node]:
                for i in range(0,len(p)-1):
                    edge = (p[i], p[i+1])
                    visitEdge[edge] = True


            for x in d[node]:
                if not v[x]:
                    DFS(x,p[:])


        DFS(0,[])

        return (2*len(visitEdge))
