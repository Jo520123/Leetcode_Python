class Solution:
    def maxSum(self, nums1 , nums2):
        """
        :param nums1: List[int]
        :param nums2: List[int]
        :return: int
        """
        n1_s, n2_s = 0, 0
        n1_e, n2_e = len(nums1), len(nums2)
        n1_count, n2_count = 0, 0


        while n1_s < n1_e or n2_s < n2_e:
            if n1_s < n1_e and (n2_s == n2_e or nums1[n1_s] < nums2[n2_s]) :
                n1_count += nums1[n1_s]
                n1_s += 1

            elif n2_s < n2_e and (n1_s == n1_e or nums2[n2_s] < nums1[n1_s]) :
                n2_count += nums2[n2_s]
                n2_s += 1

            else:
                n1_count = n2_count = max(n1_count, n2_count) + nums2[n2_s]
                n1_s += 1
                n2_s += 1


        return max(n1_count, n2_count) % (10**9 +7)
