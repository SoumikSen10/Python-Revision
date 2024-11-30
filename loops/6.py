# Keep asking for input unless no. entered between 1 and 10

n = int(input("Enter a number : "))

if 1 <= n <= 10:
    print("Thanks") 
else : 
 print("Invalid! Try again")   
 while True:
   n = int(input("Enter a number : ")) 
   if 1 <= n <= 10:
    print("Thanks") 
    break  
   else :
       print("Invalid! Try again")
   
