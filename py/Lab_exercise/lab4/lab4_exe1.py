n=int(input("Please enter a positive odd integer: "))
while n%2==n & n<=0:
    n=int(input("Please enter a positive odd integer: "))
ans=sum(range(1,n+1,2))
for i in range(1,n,2):
    print(f"{i} +",end=' ')
print(f"{n} = {ans}",end=' ')