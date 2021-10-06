from collections import deque

class FirstUnique:
    def __init__(self, nums):
        """
        :param nums:  List[int]
        """
        self.q = deque(nums)

    def showFirstUnique(self):
        """
        :return: int
        """
        for x in self.q:
            if self.q.count(x) == 1:

                return x

        return -1

    def add(self, value):
        """
        :param value: int
        :return: None
        """
        self.q.append(value)
