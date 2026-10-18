numbers=[]
for i in range(1,6):

    if i==1:
        print("Please enter the 1st number: ")
    elif i==2:
        print("lease enter the 2nd number: ")
    elif i==3:
        print("Please enter the 3rd number: ")
    else:
        print(f"Please enter the {i}th number: ")
    
    num=int(input())
    numbers.append(num)

ans=numbers[1]

for i in range(5):
    if numbers[i]>ans:
        ans=numbers[i]
print(f"The biggest number among {numbers} is {ans}.")