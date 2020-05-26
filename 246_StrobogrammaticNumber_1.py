def Strogogrammatic_num(n):
    result = num_def(n,n)
    return result

def num_def(n, length):
    if n == 0: return [""]
    if n == 1: return ["1","0","8"]

    middles = num_def(n-2, length)
    print(middles)
    result= []

    for m in middles:
        if n != length:
            result.append("0" + m +"0")
        result.append("8" + m +"8")
        result.append("1" + m + "1")
        result.append("9" + m + "6")
        result.append("6" + m + "9")

    return result
