import collections

class TwoSum:

    def __init__(self):
        self.record = collections.defaultdict(int)

    def add(self, n):
        self.record[n] += 1

    def find(self,value):
        r = self.record
        for num in r :
            l = value-num
            if l != num and l in r or l == num and r[num] > 1:

                return True
        return False
