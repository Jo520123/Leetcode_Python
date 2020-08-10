# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):
        """
        :param head:  'Node'
        :return:  'Node'
        """
        if not head:
            return None

        dummy = copy_list = Node(1,None,None)
        d = dict()

        while head:
            if head in d:
                copy_list.next = d[head]
            else:
                n = Node(head.val, None, None)
                d[head] = n
                copy_list.next = n

            if head.random in d:
                copy_list.next.random = d[head.random]

            elif head.random:
                n = Node(head.random.val, None, None)
                d[head.random] = n
                copy_list.next.random = n

            copy_list = copy_list.next
            head = head.next

        return dummy.next







































h = {}
print(type(h))
h[0] = 1
print(h)


g = dict()
print(type(g))
g[0] = 8
print(g)


