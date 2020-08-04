from collections import defaultdict
from collections import deque
class Solution:
    def validTree(self, n, edges):
        """
        :param n: int
        :param edges: List[List[int]]
        :return: bool
        """
        if len(edges) != n-1:
            return False


        adj_liast = defaultdict(list)
        v = {}
        q = deque([0])

        for x,y in edges:
            adj_liast[x].append(y)
            adj_liast[y].append(x)

        while q:
            node = q.popleft()
            v[node] = True

            for x in adj_liast[node]:
                if x not in v:
                    v[x] = True
                    q.append(x)

        return len(v) == n
