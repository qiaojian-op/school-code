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