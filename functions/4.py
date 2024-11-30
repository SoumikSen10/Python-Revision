import math

def circle_stats(r) :
    return math.pi * r **2 , 2*math.pi*r
    
r = int(input("Enter radius : "))    

area , circumference = circle_stats(r)
print("Area and circumference are : " ,area , circumference)