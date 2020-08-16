class Solution:
    def findKthPositive(self, arr , k):
        """
        :param arr: List[int]
        :param k: int
        :return: int
        """
        start, end = 0, len(arr)

        while start < end:
            m = (start + end)//2
            if arr[m] - (m + 1) < k:
                start = m + 1
            else:
                end = m
        return start + k

arr1 = [1,2,3,4]
k1 = 2

x = Solution()
arr = [2,3,4,7,11]
k = 5
#Output: 9
print(x.findKthPositive(arr, k))

arr1 = [1,2,3,4]
k1 = 2
#Output: 6
print(x.findKthPositive(arr1, k1))
