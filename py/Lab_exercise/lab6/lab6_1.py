def countdown(n):
    if n==0:
        print("Countdown complete!")
    else:
        print(n,end=" ")
        countdown(n-1)

def main():
    num = int(input("Enter a number to countdown from: "))
    countdown(num)
main()  