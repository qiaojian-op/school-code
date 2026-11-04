def sum_multiply(a,b,s=0):
    if s==0:
        return a+b
    elif s==1:
        return a*b
    else:
        print("Invalid Input")
        return 0
print("Please enter three numbers:num1 num2 options")
print("0:num1 + num2")
print("1:num1 x num2")
num1=int(input("num1: "))
num2=int(input("num2: "))
option=int(input("option: "))
ans=sum_multiply(num1,num2,option)
print(ans)