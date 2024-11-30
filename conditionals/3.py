# Password Checker

password = input("Enter a password : ")

n = len(password)

if n < 6 :
    print("Weak")
elif n >= 6 and n <= 10 :
    print("Medium")
else :
    print("Strong")        