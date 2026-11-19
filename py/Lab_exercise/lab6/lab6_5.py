import recursiveFunctions as rf

def main():
    while True:
        print("====menu====")
        print("1. Factorial")
        print("2. Fibonacci")
        print("3. Countdown")
        print("4. Exit")
        print("============")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            n = int(input("Enter a number: "))
            print("Factorial of", n, "is", rf.factorial(n))
        elif choice == 2:
            n = int(input("Enter a number: "))
            print("Fibonacci of", n, "is", rf.fibonacci(n))
        elif choice == 3:
            n = int(input("Enter a number: "))
            rf.countdown(n)
        else:
            print("Exiting...")
            break
main()