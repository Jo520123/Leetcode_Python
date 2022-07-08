from collections import defaultdict
class Solution:
    def restoreArray(self, adjacentPairs):
        """
        :param adjacentPairs: List[List[int]
        :return: List[int]
        """
        d = defaultdict(list)
        ans = []

        for x in adjacentPairs:
            d[x[0]].append(x[1])
            d[x[1]].append(x[0])

        for x, y in d.items():

            if len(y) == 1:
                ans.append(x)

                break

        ans.append(d.get(ans[0])[0])


        for i in range(2, len(adjacentPairs)+1):
            p = ans[-1]

            if d[p][0] == ans[-2]:
                ans.append(d[p][1])

            else:
                ans.append(d[p][0])

        return ans
