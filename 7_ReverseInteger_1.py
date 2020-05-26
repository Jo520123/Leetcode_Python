def reverse(x):
    """
            :type x :int
            :rtype: int
        """

    if x>=0:
        x=int(str(x)[::-1])
    else:
        x=-int(str(-x)[::-1])
    return x if x<=(1<<31)-1 and x>=-(1<<31) else 0


print(reverse(123))
print(reverse(-123))



