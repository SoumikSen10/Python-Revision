# Factorial of number

n = int(input("Enter a number : "))

f = 1

""" for i in range(1,n+1):
    f=f*i
    
print("Factorial of number is : ",f)     """

# Using while loop

i = 1

while(i!=n+1):
    f = f * i
    i = i + 1

print(f)    
    