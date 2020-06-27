# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :param l1: ListNode
        :param l2: ListNode
        :return: ListNode
        """
        if l1 == None:
            return l2
        if l2 == None:
            return l1

        dummy = ListNode(0)
        a = dummy
        car = 0

        while l1 and l2:
            a.next = ListNode((l1.val + l2.val + car)%10)
            car = (l1.val + l2.val + car)//10
            l1 = l1.next
            l2 = l2.next
            a = a.next

        if l1:
            while l1:
                a.next = ListNode((l1.val + car) % 10)
                car = (l1.val + car) // 10
                l1 = l1.next
                a = a.next

        if l2:
            while l2:
                a.next = ListNode((l2.val + car) % 10)
                car = (l2.val + car) // 10
                l2 = l2.next
                a = a.next

        if car == 1:
            a.next = ListNode(1)

        return dummy.next

