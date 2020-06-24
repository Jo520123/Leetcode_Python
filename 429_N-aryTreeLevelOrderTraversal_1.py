# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root):
        """
        :param root: Node
        :return: List[List[int]
        """
        if root == None:
            return []

        current =[root]
        next =[]
        result =[]

        while current:
            temp = []
            for x in current :
                temp.append(x.val)
                for y in  x.children:
                    next.append(y)

            result.append(temp)
            current = next
            next = []

        return result
