from collections import defaultdict

class Solution:
    def canArrange(self, arr, k):
        """
        :param arr: List[int]
        :param k: int
        :return:bool
        """

        d = defaultdict(int)

        for x in arr:

            d[x%k] += 1


        if 0 in d:

            if d[0]%2 != 0:

                return False

            del d[0]



        for x in d :

            if d[x] != d[k-x]:

                return False

        return True
