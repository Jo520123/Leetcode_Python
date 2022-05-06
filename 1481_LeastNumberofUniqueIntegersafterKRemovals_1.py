class Solution:
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :param arr:  List[int]
        :param k: int
        :return: int
        """

        d = {}

        for x in arr:
            if x not in d:
                d[x] = 1

            else:
                d[x] += 1

        l = len(d)

        ascd = sorted(d.items(), key = lambda y:y[1])

        for x ,y in ascd:

            if y <= k:
                k -= y
                l -= 1
            else:
                break

        return l
