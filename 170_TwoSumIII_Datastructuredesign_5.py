class Solution:

    def __init__(self):
        self.store = {}


    def add(self, number):
        if number not in self.store:
            self.store[number] = 1

        else:
            self.store[number] += 1

    def find(self, value):
        for x in self.store:
            if value - x in self.store and (value-x != x or self.store[x] > 1):
                return True

        return False
