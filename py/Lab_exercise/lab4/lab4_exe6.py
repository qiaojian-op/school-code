print("=== MENU ===")
print("""
1.Generate Multiplication Table
2.Run Countdown
3.Exit
Select an option(1-3): 
""")
k=int(input())
if k==3:
    print("Goodbye!")
else:
    while True:
        if k==2:
            s=int(input("Please enter a starting number: "))
            for i in range(s,0,-1):
                print(i,end=' ')
            print('\n')
        elif k==1:
            a=int(input("Enter table number: "))
            b=int(input("Enter limit: "))
            for i in range(1,b+1):
                print(f"{a} x {i} = {a*i}")
        k=int(input("Select an option(1-3): "))
        if k==3:
            print("Goodbye!")
            break