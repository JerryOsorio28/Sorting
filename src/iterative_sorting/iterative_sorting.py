# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    #loops through the array 
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        #loops through the array right to the initial for loop
        for x in range(cur_index, len(arr)):
            #if smallest value on index 0 > than the value of array in x position, assign smallest.
            if arr[smallest_index] > arr[x]:
                smallest_index = x
        #holds temporarly the index in position smallest_index
        temp = arr[smallest_index] 
        #switchs whatever is on the smallest index to the current index that checked (on the if statement) that it was less than smallest_index.
        arr[smallest_index] = arr[cur_index]
        #switchs whatever is on current index with whatever it was on the smallest index.
        arr[cur_index] = temp

    return arr
 
print('result', selection_sort([5,6,9,4,3,1,2,0,8,7]))
# TO-DO: implement the Bubble Sort function below
def bubble_sort( arr ):
    #boolean to turn off while loop
	arr_sorted = True
    #conditional statement to run it while true
	while arr_sorted:
        #sets condition to false
		arr_sorted = False
        #iterate through the array
		for x in range(0, len(arr) - 1):
			#REMEMBER -- i and x are the INDEX, arr[i] and arr[x] are the VALUES
            #checks if current index value is greater than next index
			if arr[x] > arr[x + 1]:
                #grabs current index value
				temp = arr[x] #7
                #assign current index value to the next index value--|
				arr[x] = arr[x + 1]                                 #SWAPS
                #assign next index value to the current index value--|
				arr[x + 1] = temp
                #if it finds current index value greater than next index value, turn on while loop.
				arr_sorted = True
    #returns sorted array
	return arr


# STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):

#     return arr