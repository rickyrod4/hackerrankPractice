#Buble Sort
#Given an array sort thru by swapping each pair


def bubbleSort(arr):
    print('Original Array:', arr)
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]

    print('New Array:', arr)
bubbleSort([8,7,2,6,4])