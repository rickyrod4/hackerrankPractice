



def swap_case(s):
    print('Original string: ', s)
    new_string = ''
    for character in s:
        if character.islower() == True:
            new_string += character.upper()
        else:
            new_string += character.lower()
    print('New String', new_string)
    return new_string

swap_case("heLLo World")

from collections import Counter

array1 = [1,2,3,5,5,47,2]
print(Counter(array1))

dict1 = {}
for item in array1:
    if item in dict1:
        dict1[item] += 1
    else:
        dict1[item] = 1
print(dict1)

for value in dict1:
    if dict1[value] >1:
        print(value)