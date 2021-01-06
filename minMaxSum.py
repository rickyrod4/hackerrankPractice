#given five positive integers, find the minimum and maximum values that 
#can be calculated by summing exactly four of the five integers. 
#Then print the respective minimum and maximum
#valuse as a single line of two space-separated long integers

def minMaxSum(arr):
    minSum = 0
    maxSum = 0
    sum = 0
    for item in arr:
        sum += item

    print(sum)
    


minMaxSum([1,3,5,7,9])