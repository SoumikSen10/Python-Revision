# Reverse a string

str = input("Enter a string : ")

n = len(str)

new_str = ""

for i in range(0,n):
    new_str = str[i] + new_str
    
print("Reversed string is : ",new_str)    