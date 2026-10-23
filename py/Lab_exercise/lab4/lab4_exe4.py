n=int(input("Please enter a positive odd number: "))
t=(n+1)//2
space=0
for i in range(t):
    print(" "*space,end='')
    space=space+1
    print("*"*n)
    n=n-2