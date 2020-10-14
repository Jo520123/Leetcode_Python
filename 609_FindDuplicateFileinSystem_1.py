from collections import defaultdict
class Solution:
    def findDuplicate(self, paths):
        """
        :param paths: List[str]
        :return:  List[List[str]]
        """
        table = defaultdict(list)
        ans = []

        for x in paths:
            doc = x.split()
            r = doc[0]

            for y in doc[1:]:
                i, j ,k  = y.partition('(')
                table[k[:-1]].append(r + '/' +i)



        for v in table.values():
            if len(v) > 1:
                ans.append(v)
        return ans
