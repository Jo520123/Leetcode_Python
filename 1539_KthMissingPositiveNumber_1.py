class Solution:
    def findKthPositive(self, arr , k):
        """
        :param arr: List[int]
        :param k: int
        :return: int
        """
        n = 1
        ans = 0
        for i in range(len(arr)):
            while k != 0 and arr[i] != n:
                ans = n
                k -= 1
                n += 1

            if k == 0:
                return ans

            else:
                n += 1

        ans = n-1
        while k > 0:
            ans += 1
            k -= 1

        return ans
