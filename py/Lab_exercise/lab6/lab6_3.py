def fib(n):
    global calls
    calls+=1
    if n==0:
        return 0;
    elif n==1:   
        return 1;
    else:
        return fib(n-1)+fib(n-2)

def main():
    global calls
    calls = 0
    n=int(input("Enter a number to calculate its Fibonacci: "))
    print("Index\tFibonacci\tNumbers of Calls")
    for i in range (0,n+1):
        print(f"{i}\t{fib(i)}\t\t{calls}")
        calls=0
main()