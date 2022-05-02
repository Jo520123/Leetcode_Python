class Solution:
    def minSumOfLengths(self, arr, target):
        """
        :param arr: List[int]
        :param target: int
        :return: int
        """

        ans = float('inf')
        l = len(arr)
        total = 0
        pp = 0
        table = [float('inf')] * l
        minl = float('inf')

        for i in range(l):
            total += arr[i]

            while(total > target):

                total -= arr[pp]
                pp += 1


            if (total == target):
                cur  = i - pp + 1

                if (pp > 0):
                    ans  = min(ans, cur + table[pp-1])

                minl = min(minl,cur)

            table[i] = minl


        if (ans == float('inf')):
            return -1

        else:
            return ans
