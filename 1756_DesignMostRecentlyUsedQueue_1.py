from sortedcontainers import SortedList

class MRUQueue:
    def __init__(self, n):
        """
        :param n: int
        """

        self.sL = SortedList((x-1,x) for x in range(1,n+1))

    def fetch(self, k):
        """
        :param k: int
        :return:int
        """
        lastIDX, lastVal = self.sL[-1]
        pIdx, pVal = self.sL.pop(k-1)

        self.sL.add((lastIDX+1,pVal))
        print(pVal)
        return pVal
