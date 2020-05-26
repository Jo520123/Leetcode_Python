class Solution:
    def CountPrimes(self, x):
        """
               :type x: int
               :rtype: int
               """
        if x <2 :
            return 0

        digits = [1]*x
        digits[0] = digits[1] = 0

        for i in range(2, int(x**0.5)+1):
            if digits[i] == 1:
                for j in range(i+i, x,i):
                    digits[j] = 0
        return sum(digits)
