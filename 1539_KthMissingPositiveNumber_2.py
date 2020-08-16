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
