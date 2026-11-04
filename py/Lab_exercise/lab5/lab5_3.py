def revers_string(x):
    y=''
    for ch in  x:
        y=ch+y
    return y
a=[]
a=input("Please enter a string: ")
b=revers_string(a)
print(f"Original: {a}")
print(f"Reversed: {b}")