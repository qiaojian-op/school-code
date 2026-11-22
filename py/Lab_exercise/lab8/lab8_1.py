def Get_marks(marks=[]):
    marks=list(map(int,input("Enter marks of student {}: ").split()))
    return marks

def main():
    marks=[]
    marks=Get_marks(marks)
    print("Original marks: ",marks)
    print("Highest marks: ", max(marks))
    print("Lowest mark: ", min(marks))
    ave=sum(marks)/len(marks)
    print("Average mark: ",ave)
    print("Passing marks: ")
    for i in marks:
        if i>=60:
            print(i,end=" ")
    marks.sort(reverse=True)
    print("Descending order: ",marks)
    print("First three marks: ",marks[:3])
    print("Last three marks: ",marks[-3:])

main()