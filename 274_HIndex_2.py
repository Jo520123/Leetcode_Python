#时间复杂度是O(NlogN + logN)，空间复杂度是O(N)。
class Solution:
    def hIndex(self, citations):
        """
        :param citations: List[int]
        :return: int
        """
        idx_len = len(citations)
        citations.sort()
        l,r = 0, idx_len-1
        ci_amount = 0

        while l <= r:
            m = (l + r)//2
            ci_amount = max(ci_amount, min(citations[m], idx_len - m))

            if  citations[m] < idx_len - m:
                l = m + 1
            else:
                r = m - 1

        return ci_amount
