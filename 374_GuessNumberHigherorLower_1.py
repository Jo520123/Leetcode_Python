class Solution:
    def GuessNumber(self, x):
        """
        :type x: int
        :rtype: int
        """
        l, r = 0, x
        while True:
            mid = (l+r)//2
            if guess(mid) == 1:
                l = mid + 1
            elif guess(mid) == -1:
                r = mid -1
            else:
                return mid
