# Sum of even and odd nums

n = int(input("Enter a number : "))

# Initialize counters for even and odd numbers
evens = 0
odds = 0

for i in range(1,n+1) : 
    if i % 2 == 0 :
        evens = evens + 1
    else :
        odds = odds + 1

print("Even : ",evens,"Odd : ",odds)            
        