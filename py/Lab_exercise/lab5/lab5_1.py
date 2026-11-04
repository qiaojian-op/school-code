def SUM(n):
    sum=0
    for i in range(1,n,2):
        sum=sum+i
        print(f"{i} + ",end="")
    sum=sum+n
    return sum

num=int(input("Please enter a odd number: "))
ans=SUM(num)
print(f"{num} = {ans}")