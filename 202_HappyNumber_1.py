def NumSquareSum(x):
    square_Sum = 0
    while (x):
        square_Sum += (x % 10) * (x % 10)
        x = int(x/10)
    return square_Sum


def isHappynumber(x):
    slow = x
    fast = x
    while(True):
        slow = NumSquareSum(slow)
        fast = NumSquareSum(NumSquareSum(fast))
        if(slow != fast):
            continue
        else:
            break

    return (slow == 1)





















