import collections
import bisect

class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.valueTable = collections.defaultdict(list)
        self.timeTable = collections.defaultdict(list)
        self.currentTimeTable = collections.defaultdict(int)

    def set(self, key, value, timestamp):
        """
        :param key:  str
        :param value:  str
        :param timestamp: int
        :return: None
        """
        self.valueTable[key].append(value)
        self.timeTable[key].append(timestamp)
        self.currentTimeTable[key] = max(timestamp, self.currentTimeTable[key])


    def get(self, key, timestamp):
        """
        :param key: str
        :param timestamp: int
        :return: str
        """
        if key not in self.valueTable:
            return ""

        if timestamp >= self.currentTimeTable[key]:
            return self.valueTable[key][-1]

        bi_right = bisect.bisect_right(self.timeTable[key], timestamp)

        if bi_right:
            return self.valueTable[key][bi_right-1]
        else:
            return ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

x = TimeMap()
print(x.set("foo","bar",1))
x.set("foo","bar",1)
print(x.get("foo",1))
x.get("foo",1)
print(x.get("foo",3))
x.get("foo",3)
print(x.set("foo","bar2",4))
x.set("foo","bar2",4)
print(x.get("foo",4))
x.get("foo",4)
print(x.get("foo",5))
x.get("foo",5)

#inputs = ["TimeMap","set","get","get","set","get","get"]
#inputs = [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
##Output: [null,null,"bar","bar",null,"bar2","bar2"]






