def factorial(n):
    global calls
    calls+=1
    if n==0:
        print("Calling factorial(0)")
        return 1;
    else:
        print(f"Calling factorial({n-1})")
        return n*factorial(n-1)

def main():
    num = int(input("Enter a number to calculate its factorial: "))
    result = factorial(num)
    print(f"Factorial of {num} = {result}")
    print(f"Total function calls= {calls}")

calls=0
main()