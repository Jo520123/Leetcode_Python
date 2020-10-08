from collections import defaultdict
class Solution:
    def frequencySort(self, s):
        """
        :param s: str
        :return: str
        """

        result = ""
        s_set = set(s)
        table  = defaultdict(list)

        for x in s_set:
            freq = s.count(x)
            table[freq].append(x)


        for i in sorted(table.keys(), reverse = True):
            while len(table[i]) > 0:
                freq = table[i].pop()
                result += i*freq


        return result
