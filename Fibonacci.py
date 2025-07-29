n=int(input("Enter the number="))
a,b=0,1
fib=[]
for i in range(n):
    a,b=b,a+b
    fib.append(a)
print(fib) 
fib.reverse()
print("reversed",fib)   