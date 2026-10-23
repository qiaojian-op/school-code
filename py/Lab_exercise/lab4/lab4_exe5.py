a=input()
numbers=[]
for i in map(int, a.split(",")):
    numbers.append(i)
print(f"Checking list: {numbers}")
for num in numbers:
    if num<0:
        print(f"Skipping negative value: {num}")
    elif num%2==1:
        print(f"Found odd number: {num}")
    else:
        continue