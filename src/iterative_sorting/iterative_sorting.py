# TO-DO: Complete the selection_sort() function below 
def selection_sort(arr):
    # we iterate over the array
    for i in range(0, len(arr) - 1):
        # set the smallest value to be the current index
        smallest = i
        # second loop to compare values with i as we iterate
        for j in range(i, len(arr)):
            # if whats on index j is less than what it is currently consider as the smallest...
            if arr[j] < arr[smallest]:
                # we set the smallest to be the current index
                smallest = j
        # once we have the true smallest value, we grab the value of index i first...
        temp = arr[i]
        # we swap by setting what's currently the value of i to be the new smallest..
        arr[i] = arr[smallest]
        # then we swaps what's the smallest to be what is temp (which is what it was the value of i)
        arr[smallest] = temp
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    # first iterator is to keep a track of the numbers than has been sorted (bubbled up)
    for i in range(0, len(arr) - 1):
        # second iterator is to make a comparison between the current index and the index after that..
        for j in range(0, len(arr) - 1 - i):
            # if it is greater..
            if arr[j] > arr[j + 1]:
                # we swap places...
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr