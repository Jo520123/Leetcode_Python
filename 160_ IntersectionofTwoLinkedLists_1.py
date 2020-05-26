class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def GetIntersectionNode(self, hA, hB):
        """
        :type hA, hB: ListNode
        :rtype: ListNode
        """
        if hA ==None or hB ==None:
            print("1")
            return None

        A_pointer = hA
        B_pointer = hB

        while A_pointer != B_pointer:
            A_pointer = hB if A_pointer == None else A_pointer.next
            B_pointer = hA if B_pointer == None else B_pointer.next

        return A_pointer
