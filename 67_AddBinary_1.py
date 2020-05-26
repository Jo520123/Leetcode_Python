def Add_Binary_Nums(x,y):
    maxlen = max(len(x),len(y))

    x = x.zfill(maxlen)
    y = y.zfill(maxlen)
    result = ''
    carry = 0

    for i in range(maxlen-1,-1,-1):
        a = carry
        a += 1 if x[i] == '1' else 0
        a += 1 if y[i] == '1' else 0
        result = ('1' if a % 2 == 1 else '0' ) + result
        carry = 0 if a<2 else 1

    if carry !=0:
        result = '1' +result
    return result.zfill(maxlen)


