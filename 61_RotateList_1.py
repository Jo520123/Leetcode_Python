# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def rotateRight(self, head, k):
        """
        :param head: ListNode
        :param k:  int
        :return: ListNode
        """
        if head is None or head.next is None:
            return head

        p = head
        c = 0
        while p:
            c += 1
            p = p.next

        k = k % c

        if k == 0:
            return head

        p1 ,p2 =head, head
        for i in range(k):
            p1 = p1.next

        while p1 and p1.next:
            p1 = p1.next
            p2 = p2.next

        result = p2.next
        p2.next = None
        p1.next = head

        return result
