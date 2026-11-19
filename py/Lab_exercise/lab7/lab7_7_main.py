from MyPackage.Rectangle import rectangle
from MyPackage.Student import Student

def main():
    R=rectangle(10,13)
    S=Student("AIT2609028","HQJ",101)
    print(f"Area: {R.GetArea()}")
    print(f"Perimeter: {R.GetPerimeter()}")
    S.DisplayInfo()
    print(f"Grade: {S.GetGrade()}")

main()