import math
import random


def saveThePrisoner(n,m, s):
    #n = number of prisoners
    #m = number of treats
    #s = where the treats will start being passed out. 
    
    #create an array to store the treats being passed out to the prisoner
    # Use a  for loop 
    m = m%n
    s = s + m -1
    if s > n:
        s = s - n
    

    return s

print(saveThePrisoner(352926151, 380324688, 94730870))