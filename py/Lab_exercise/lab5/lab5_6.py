def calculate_stats(*args):
    count=len(args)
    if count==0:
        return (0,0,0)
    sums=sum(args)
    average=sums/count
    return (count,sums,average)

numbers=list(map(int,input().split()))
count,sums,average=calculate_stats(*numbers)
print(f"count: {count}")
print(f"sum: {sums}")
print(f"average: {average}")
