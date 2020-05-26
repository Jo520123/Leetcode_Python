def Merge_Sorted_Lists(A,B, sorted_list = None):
    if sorted_list == None:
        sorted_list =[]

    index = 0
    for elements in A:
        if elements <= B[0]:
            sorted_list.append(elements)
            index +=1
        else:
            return Merge_Sorted_Lists(B, A[index:], sorted_list)
    return sorted_list + B


