class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

class Solution:
    def HasCycle(self, head):
        if not head or not head.next:
            return False
        slow, fast = head, head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow, fast =slow.next, fast.next.next
        return True

