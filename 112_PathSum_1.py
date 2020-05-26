class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def HasPathSum(node,s):

    if node is None:
        return False
    else:
        a = 0

        subSum = s - node.data

        if (subSum ==0 and node.left == None and node.right == None):
            return True

        if node.left is not None:
            a = a or HasPathSum(node.left, subSum)
        if node.right is not None:
            a = a or HasPathSum(node.right, subSum)
        return a
