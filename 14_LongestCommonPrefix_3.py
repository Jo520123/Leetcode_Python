def LongestCommonPrefix(strs):
    prefix=""
    if len(strs)== 0: return prefix

    for i in range(len(min(strs))):
        x= strs[0][i]
        if all (a[i]==x for a in strs):
            prefix+=x
        else:
            break
    return prefix
