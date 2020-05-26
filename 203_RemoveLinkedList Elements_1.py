# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def removeElements(self,head, val):
        """
               :type head: ListNode
               :type val: int
               :rtype: ListNode
               """
        new_head = pre = ListNode(0)
        pre.next = head

        while head:
            if head.val == val:
                pre.next = head.next
            else:
                pre = pre.next
            head = head.next
        return  new_head.next

x = Solution()
a = [1, 2, 6, 3, 4, 5, 6]
val = 6
print(x.removeElements(a,val))
