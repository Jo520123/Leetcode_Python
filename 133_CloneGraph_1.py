# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node):
        """
        :param node: 'Node'
        :return: 'Node'
        """
        d = dict()
        nc = self.DFS(node, d)

        return nc

    def DFS(self, node, d):
        if not node :
            return None

        if node in d:
            return d[node]

        nc = Node(node.val, [])
        d[node] = nc

        for x in node.neighbors:
            xc = self.DFS(x, d)
            if xc:
                nc.neighbors.append(xc)
        return nc
