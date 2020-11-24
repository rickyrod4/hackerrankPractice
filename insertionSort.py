##[8,4,2,3,7]

def insertionSort(arr):
    print('Original Array:', arr)
    for i in range(len(arr)-1):
        for j in range(i+1,0,-1):
            if arr[j] < arr [j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                print('Switch Happened!!!!')
            else:
                print('No Switch')
            print("Iteration j:",j,"i:",i)
            print('Array:', arr)
            print('---------------------------')
        print('*'*15)
    print('New Array:', arr)

insertionSort([8,4,2,3,7])

#c++
