class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self,x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if not self.min:
            self.min.append(x)
        else:
            self.min.append(min(self.min[-1],x))

    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop()
        self.min.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype:int
        """
        return self.min[-1]


