# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def swapPairs(self, head):
        """
        :param head: ListNode
        :return: ListNode
        """
        if not head or not head.next:
            return head

        pt = head
        new = pt.next

        while(True):
            a = pt.next
            b = a.next
            a.next = pt

            if not b or not b.next:
                pt.next = b
                break

            pt.next = b.next
            pt = b

        return new

    