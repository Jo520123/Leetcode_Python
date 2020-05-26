def IsPalindrome( x):
        """
               :type x: int
               :rtype: bool
               """
        return str(x)==str(x)[::-1]

print(IsPalindrome(1221))
print(IsPalindrome(12421))
print(IsPalindrome(12345))

