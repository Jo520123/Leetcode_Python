from collections import defaultdict
class Solution:
    def numTriplets(self, nums1, nums2):
        """
        :param nums1: List[int]
        :param nums2: List[int]
        :return: int
        """

        def equal(nums1, nums2):

            d = defaultdict(int)
            l = len(nums2)
            reault = 0

            for x in nums1:
                d[pow(x,2)] += 1

            for i in range (l):
                for j in range (i+1,l):

                    value = nums2[i] * nums2[j]

                    if value in d:
                        reault += d[value]

            return reault


        ans = 0

        ans += equal(nums1,nums2)
        ans += equal(nums2, nums1)


        return ans
