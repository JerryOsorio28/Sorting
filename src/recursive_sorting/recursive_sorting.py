import random
arr_numbers = list(range(1, 11))
random.shuffle(arr_numbers)

def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    # we iterate over the arrays
    for i in range(0, len(merged_arr)):
    	# we check if the first array has reached the length of 0, if it has, we append everything on arrB
        if len(arrA) == 0:
            merged_arr.append(arrB[0])
            del arrB[0]
            del merged_arr[0]
        # we check if the second array has reached the length of 0, if it has, we append everything on arrA
        elif len(arrB) == 0:
            merged_arr.append(arrA[0])
            del arrA[0]
            del merged_arr[0]
        # if any of the arrays have reached length of 0...
        else:
        	#  we check if the current value in arrA is greater than value in arrB
            if arrA[0] > arrB[0]:
            	# if it is, we append the current the current value in arrB
                merged_arr.append(arrB[0])
                # and remove the value from the array
                del arrB[0]
                del merged_arr[0]
            #  we check if the current value in arrA is less than value in arrB
            elif arrA[0] < arrB[0]:
            	# if it is, we append the current the current value in arrA
                merged_arr.append(arrA[0])
                # and remove the value from the array
                del arrA[0]
                del merged_arr[0]

    return merged_arr

def merge_sort(arr):
    # first thing we need to do is split the array in the middle as long as the array is greater than 0

    # BASES CASES
    if len(arr) == 1:
        return arr
    if len(arr) == 0:
    	return arr
    else:
        # we declare our middle
        middle = len(arr) // 2
        # we call recursively and set arrA to be the array's middle, all the way until to reaches length of 1
        arrA = merge_sort(arr[:middle])
        # we call recursively and set arrB to be the array's middle, all the way until to reaches length of 1
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
