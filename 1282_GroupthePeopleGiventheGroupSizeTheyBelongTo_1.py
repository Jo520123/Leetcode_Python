from collections import defaultdict
class Solution:
    def groupThePeople(self, groupSizes):
        """
        :param groupSizes:  List[int]
        :return: List[List[int]]
        """
        sublist = defaultdict(list)
        ans = []

        for x, y in enumerate(groupSizes):
            sublist[y].append(x)

            if len(sublist[y]) == y:
                ans.append(sublist.pop(y))

        return ans
