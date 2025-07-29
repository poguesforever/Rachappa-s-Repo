print("Enter 1 to find the range of even or odd numbers.")
print("Enter 2 to find the given no. is even or odd")

x=int(input("Enter the operation="))

if x==1:
 n=int(input("Enter the range of numbers="))
 for i in range(n):
   if i%2==0:
     print("Even number=",i)
   else:
     print("Odd Number=",i)   
elif x==2:
  n=int(input("Enter the number="))
  if n%2==0:
    print("The number is Even")
  else:
    print("The number is Odd")  