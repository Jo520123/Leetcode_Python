class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None


    def IsPalindromeUtil(self, string):
        return (string == string[::-1] )


    def IsPalindrome(self):
        node = self.head

        temp =[]
        while (node is not None):
            temp.append(node.data)
            node = node.next

        string = "".join(temp)

        return self.IsPalindromeUtil(string)


    def printList(self):
        temp = self.head
        while(temp):
            temp = temp.next

