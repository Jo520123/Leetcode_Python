import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.cap = 0
        self.unique_store = set()



    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
         :param val: int
         :return: bool
        """
        if val not in self.unique_store:
            self.unique_store.add(val)
            self.cap += 1

            return True

        return False




    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :param val: int
         :return: bool
        """
        if val in self.unique_store:
            self.unique_store.remove(val)
            self.cap -= 1

            return True

        return False


    def getRandom(self):
        """
        Get a random element from the set.
         :return: int
        """
        idx = random.randint(0, self.cap-1)
        return list(self.unique_store)[idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
