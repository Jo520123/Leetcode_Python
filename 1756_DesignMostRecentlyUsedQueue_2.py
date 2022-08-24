from collections import deque
from math import ceil

class MRUQueue:
    def __init__(self, n):
        """
        :param n: int
        """
        self.d = [deque() for i in range((ceil(n**0.5)))]

        for i in range(n):
            self.d[i//len(self.d)].append(i+1)



    def fetch(self, k):
        """
        :param k: int
        :return: int
        """

        k -= 1

        idx, inidx = divmod(k,len(self.d))

        x = self.d[idx][inidx]
        del self.d[idx][inidx]

        self.d[-1].append(x)


        for i in reversed(range(idx,len(self.d)-1)):
            x1 = self.d[i+1].popleft()

            self.d[i].append(x1)

        print(x)
        return x
