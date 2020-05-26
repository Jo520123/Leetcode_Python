def RomanToInt(str):
    """
        :type str: str
        :rtype: int
        """
    if not str:
        return 0
    dic = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    n = len(str)
    total_num = dic[str[n-1]]
    for i in range(n-1,0,-1):
        cur = dic[str[i]]
        pre = dic [str[i-1]]
        total_num += pre if pre >= cur else -pre
    return total_num


