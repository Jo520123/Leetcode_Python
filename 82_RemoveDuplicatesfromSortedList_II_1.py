class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """"
            :type head: ListNode
            :rtype:  ListNode
        """
        dummy_head = ListNode(0)
        dummy_head.next = head
        pre = dummy_head
        cur = head

        while cur:

            while cur.next and cur.val == cur.next.val:
                cur = cur.next

            if pre.next == cur:
                pre = cur

            else:
                pre.next = cur.next

            cur = cur.next

        return dummy_head.next