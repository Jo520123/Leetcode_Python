class Solution:
    def numTilePossibilities(self, tiles):
        """
        :param tiles: str
        :return: int
        """

        result = []
        self.DFS('', result, tiles)
        return len(set(result))


    def DFS(self, route, result, tiles):
        if route:
            result.append(route)

        for i in range(len(tiles)):
            self.DFS(route + tiles[i], result, tiles[:i]+tiles[i+1:])
