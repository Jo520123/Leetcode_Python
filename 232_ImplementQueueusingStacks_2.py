class Queue:
    def __init__(self):
        self.s = []

    def EnQueue(self,data):
        self.s.append(data)

    def DeQueue(self):
        if len(self.s) <=0:
            print("Queue is empty")
            return
        x = self.s[len(self.s) -1]
        self.s.pop()

        if len(self.s) <=0:
            return x

        item = self.DeQueue()

        self.s.append(x)
        return item

