#Buble Sort
#Given an array sort thru by swapping each pair


def bubbleSort(arr):
    print('Original Array:', arr)
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    print('New Array:', arr)
bubbleSort([10,1,7,2,3,2,8,6,4])