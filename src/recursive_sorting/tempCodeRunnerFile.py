def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO

    for i in range(0, len(merged_arr)): #[0,0,0,0,0,0]
        if arrA[i] == 0:
            merged_arr.append[arrB[i]]
        elif arrB[i] == 0:
            merged_arr.append[arrA[i]]
        if arrA[i] < arrB[i]:
            merged_arr.append(arrA[i])
            del arrA[i]
        elif arrA[i] > arrB[i]:
    print(merged_arr)
    return merged_arr

merge([1,2,3], [4,5,6])