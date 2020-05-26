class Solution:
    def IsPerfectSquare(self, num):
        """
               :type num: int
               :rtype: bool
               """
        l, r = 0, num
        while l <= r :
            mid = (l+r) // 2
            if mid*mid >= num:
                r = mid - 1
            else:
                l = mid + 1
        return l*l == num
