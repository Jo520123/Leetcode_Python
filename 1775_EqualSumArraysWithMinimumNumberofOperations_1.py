class Solution:
    def minOperations(self, nums1, nums2):
        """
        :param nums1: List[int]
        :param nums2: List[int]
        :return: int
        """

        total1 = sum(nums1)
        total2 = sum(nums2)

        ans = 0

        nums1 = sorted(nums1)
        nums2 = sorted(nums2)


        if total1 > total2:

            total1, total2 = total2, total1
            nums1, nums2 = nums2, nums1

        l , r = 0 , len(nums2)-1

        while l < len(nums1) or r >= 0:

            if total1 == total2:

                return ans

            if l < len(nums1):
                cl = nums1[l]
            else:
                cl = 7

            if r >= 0:
                cr = nums2[r]
            else:
                cr = 0

            if 6 - cl >= cr - 1:
                total1 += min(total2-total1, 6-cl)
                l += 1

            else:
                total2 -= min(total2-total1, cr-1)
                r -= 1

            ans += 1


        if total1 != total2:

            return -1

        else:
            return ans
