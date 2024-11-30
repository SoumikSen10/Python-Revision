# polymorphism - write function that multiplies two numbers , but can also accept and multiply strings.

def multiply(a,b) :
    return a*b

a = int(input("Enter first no./char : "))
b = int(input("Enter first no./char : "))

print(multiply(a,b))

print(multiply('a',5))
print(multiply(2,'b'))