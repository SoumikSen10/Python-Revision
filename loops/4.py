# Find first non - repeated character

#Example : teeter

str = input("Enter a string : ")

for char in str:
    if str.count(char) == 1 :
        print(char)
        break
    
    