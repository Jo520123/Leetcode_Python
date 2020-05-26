def Read(buf,n):
    index = 0
    while index < n:
        buf_4 = [" "]*4
        c = read4(buf_4)
        if c== 0:
            break

        c = min(c, n-index)
        buf[index:] = buf_4[:c]
        index +=c

    return index

