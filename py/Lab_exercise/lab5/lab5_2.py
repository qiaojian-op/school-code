def Summation(s):
    ans=0
    for i in s:
        ans=ans+i
    return ans
def Multiplilcation(s):
    ans=1
    for i in s:
        ans=ans*i
    return ans

a=list(map(int,input().split()))
totsum=Summation(a)
mul=Multiplilcation(a)
print(f"SUMMATION = {totsum}")
print(f"MULTIPLICATION = {mul}")