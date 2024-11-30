day = input("Enter the day : ")

age = int(input("Enter the age : "))

if age < 18 :
    price = 8
else :
    price = 12
    
if day == "Wednesday" :
    price = price - 2
    
print(price)           