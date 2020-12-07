#given an array of n elements
#calculate the ratios of positive, negative and zero values

def plusMinus(arr):
    positiveCount = 0
    negativeCount = 0
    zeroCount = 0

    for item in arr:
        if item > 0:
            positiveCount += 1
        elif item < 0:
            negativeCount += 1
        else:
            zeroCount += 1
    
    positiveRatio = positiveCount / len(arr)
    negativeRatio = negativeCount / len(arr)
    zeroRatio = zeroCount / len(arr)

    print('%.6f'%positiveRatio)
    print('%.6f'%negativeRatio)
    print('%.6f'%zeroRatio)

plusMinus([1,1,0,-1,-1])
