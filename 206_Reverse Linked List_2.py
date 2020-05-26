class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def ReverseUtil(self, cur,pre):

        if cur.next is None:
            self.head = cur
            cur.next = pre
            return

        next= cur.next
        cur.next = pre

        self.ReverseUtil(next, cur)

    def reversed(self):
        if self.head is not None:
            return self.ReverseUtil(self.head, None)

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

