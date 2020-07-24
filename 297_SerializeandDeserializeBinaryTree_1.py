# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        ser_result = []

        def TF_ser(root):
            if root:
                ser_result.append(str(root.val))
                TF_ser(root.left)
                TF_ser(root.right)
            else:
                ser_result.append('.')

        TF_ser(root)

        return ''.join(ser_result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        temp = ""
        for d in data:
            temp = temp + str(d) + ' '

        r = iter(temp.split())

        def deser():
            nr = next(r)
            if nr == ".":
                return None

            elif nr == '-':
                nr = next(r)
                n = TreeNode(-1 * int(nr))
            else:
                n = TreeNode(int(nr))

            n.left = deser()
            n.right = deser()
            return n

        return deser()
