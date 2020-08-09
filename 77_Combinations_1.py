class Solution:
    def combine(self, n , k):
        """
        :param n: int
        :param k: int
        :return: List[List[int]]
        """
        result = []
        list = [i for i in range(1,n+1)]
        self.DFS(list, k, [], result)
        return result

    def DFS(self, list, k, route, result):
        if k > len(list):
            return

        if k == 0:
            result.append(route)

        else:
            self.DFS(list[1:], k-1, route + [list[0]], result)
            self.DFS(list[1:], k, route , result)
