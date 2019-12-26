# TO-DO: complete the merge function below to merge 2 sorted arrays
def merge( arrA, arrB ):
	elements = len( arrA ) + len( arrB )
	merged_arr = []
	# TO-DO
	for i in range(0, elements):
		if len(arrA) == 0:
			merged_arr.append(arrB[0])
			del arrB[0]
		elif len(arrB) == 0:
			merged_arr.append(arrA[0])
			del arrA[0]
		else:
			if arrA[0] < arrB[0]:
				merged_arr.append(arrA[0])
				del arrA[0]
			elif arrA[0] > arrB[0]:
				merged_arr.append(arrB[0])
				del arrB[0]
	return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    #BASE CASES
    if len(arr) == 0: 
    	return arr
    if len(arr) == 1:
    	return arr
    #sets the middle of the array
    middle = len(arr) // 2
    #we need to find the middle of the arr that is passed as a param and sort it
    arrA = merge_sort(arr[0:middle])
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
