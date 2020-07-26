from collections import deque
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root):
        """
        :param root: 'Node'
        :return: 'Node'
        """
        if root:
            if root.left and root.right:
                root.left.next = root.right
                node = root.next
                while node:
                    if node.left:
                        root.right.next = node.left
                        break
                    if node.right:
                        root.right.next = node.right
                        break
                    node = node.next

            elif root.left:
                node = root.next
                while node:
                    if node.left:
                        root.left.next = node.left
                        break
                    if node.right:
                        root.left.next = node.right
                        break
                    node = node.next

            elif root.right:
                node = root.next
                while node:
                    if node.left:
                        root.right.next = node.left
                        break
                    if node.right:
                        root.right.next = node.right
                        break
                    node = node.next

            self.connect(root.right)
            self.connect(root.left)

        return root
