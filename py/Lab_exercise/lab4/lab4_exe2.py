n=int(input("Please enter a positive integer: "))
m=n
count=0

while m!=0:
    m=m//10
    count=count+1
print(count)
print(n)
while n!=1:
    if n%2==0:
        print(n,end=',')
        n=n//2
    elif n%2==1:
        print(n,end=',')
        n=3*n+1
print('1')