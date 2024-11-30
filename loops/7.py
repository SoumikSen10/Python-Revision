# Prime no.

import math

n = int(input("Enter a number : "))

def prime(n):
        
    if n<2 :
        return False
    
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0 :
         return False
    
    return True

if prime(n) :
    print("Prime")
else :
    print("Not Prime")        


