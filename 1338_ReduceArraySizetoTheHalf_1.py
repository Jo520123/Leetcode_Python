from collections import defaultdict
class Solution:
    def minSetSize(self, arr):
        """
        :param arr: List[int]
        :return: int
        """

        d = defaultdict()
        lis = []
        sum = 0
        ans = 0

        for x in arr:
            d[x] = d.get(x,0) + 1

        for x in d:
            lis.append(d[x])

        ordlis = sorted(lis)


        for x in ordlis[::-1]:
            ans += 1
            sum += x

            if sum >= len(arr)/2:
                break


        return ans
