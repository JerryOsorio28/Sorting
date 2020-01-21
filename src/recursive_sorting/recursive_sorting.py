# TO-DO: complete the helper function below to merge 2 sorted arrays
import random
arr_numbers = list(range(1, 11))
random.shuffle(arr_numbers)
print(arr_numbers)

def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO

    for i in range(0, len(merged_arr) - 1):
        if len(arrA) == 0:
            merged_arr.extend(arrB)
            del arrB[0]
        elif len(arrB) == 0:
            merged_arr.extend(arrA)
            del arrA[0]
        else:
            if arrA[0] > arrB[0]:
                del merged_arr[0]
                merged_arr.append(arrB[0])
                del arrB[0]
            else:
                del merged_arr[0]
                merged_arr.append(arrA[0])
                del arrA[0]

    return merged_arr

def merge_sort(arr):
    # first thing we need to do is split the array in the middle as long as the array is greater than 0
    if len(arr) == 1:
        return arr
    if len(arr) == 0:
    	return arr
    else:
        # we declare our middle
        middle = len(arr) // 2
        arrA = merge_sort(arr[:middle])
        arrB = merge_sort(arr[middle:])

    return merge(arrA, arrB)

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
