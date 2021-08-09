# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeZeroSumSublists(self, head):
        """
        :param head: Optional[ListNode]
        :return: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        d = dict()
        total = 0
        start = dummy


        while start:
            total += start.val
            d[total] =start
            start= start.next

        total = 0
        s = dummy

        while s:
            total += s.val
            s.next = d[total].next
            s = s.next

        return dummy.next
