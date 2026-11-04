def unique_list(lis):
    Unique_lis=[]
    Unique_lis.append(lis[0])
    for i in range(1,len(lis)):
        if lis[i] != lis[i-1]:
            Unique_lis.append(lis[i])
    return Unique_lis
Origin_list=[]
Origin_list=list(map(int,input("Please enter a list: \n").split()))
Origin_list.sort()
print(f"The unique list is: ")
Unique_list=unique_list(Origin_list)
print(Unique_list)
