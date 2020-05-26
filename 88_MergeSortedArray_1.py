def MergeArrays(a1, a2, n1, n2):
    a3 = [None]*(n1+n2)
    i = 0
    j = 0
    k = 0

    while i < n1 and j < n2:

        if a1[i] < a2[j]:
            a3[k] = a1[i]
            k = k + 1
            i = i + 1
        else:
            a3[k] = a2[j]
            k = k + 1
            j = j + 1

    while i< n1:
        a3[k] = a1[i]
        k = k + 1
        i = i + 1

    while j< n2:
        a3[k] = a2[j]
        k = k + 1
        j = j + 1
    print("Merging Result")
    for i in range(n1 + n2):
        print(str(a3[i]), end = " ")

