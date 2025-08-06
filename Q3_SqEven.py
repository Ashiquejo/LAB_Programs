m=int(input("Enter value of m: "))
n=int(input("Enter value of n: "))
s={ i**2 for i in range(m,n+1) if i%2==0}
print("Required Set :" ,s)
