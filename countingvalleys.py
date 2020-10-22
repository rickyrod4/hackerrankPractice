
def countingValleys(steps, path):
    sea_level = 0
    valleys = 0
    for i in range(len(path)):
        if sea_level == 0 and path[i] == 'D':
            valleys += 1
            
        if path[i] == 'U':
            sea_level += 1
        else:
            sea_level -= 1
    return valleys
print(countingValleys(8, 'UDDDUDUU'))