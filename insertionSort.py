##[8,4,2,3,7]

def insertionSort(arr):
    print('Original Array:', arr)
    for i in range(len(arr)-1):
        if arr[i+1] < arr [i]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
        #for j in range(len(arr)-1-i):
    print('New Array:', arr)

insertionSort([8,4,2,3,7])

