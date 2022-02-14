class Solution:
    def countTriplets(self, arr):
        """
        :param arr:  List[int]
        :return: int
        """

        l = len(arr)
        ans = 0

        for i in range(l-1):

            x = 0

            for j in range(i, l):

                x^= arr[j]

                if x == 0:

                    ans += j -i

        return ans
