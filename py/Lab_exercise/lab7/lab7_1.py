class Student:
    def __init__(self, student_ID, name, marks):
        self.student_ID = student_ID
        self.name = name
        self.marks = marks
    def DisplayInfo(self):
        print("Student ID: ", self.student_ID)
        print("Name: ",self.name)
        print("marks: ", self.marks)
    def GetGrade(self):
        if self.marks >= 80:
            return "A"
        elif self.marks >=60:
            return "B"
        elif self.marks >=50:
            return "C"
        else:
            return "F"

def main():
    stu1 = Student("Huang Qiaojian","AIT2609028",101)
    stu1.DisplayInfo()
    print("Grade: ", stu1.GetGrade())
    
    stu2 = Student("Sathvik","AIT2609xxx",101)
    stu2.DisplayInfo()
    print("Grade: ", stu2.GetGrade())
main()
