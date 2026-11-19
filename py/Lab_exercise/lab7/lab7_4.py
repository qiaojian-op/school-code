class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def dispalySalary(self):
        print(f"{self.name}'s Salary: {self.salary} RM")

def increaseSalary(employee,amount):
    employee.salary+=amount

def main():
    S=Employee("Mike",3000)
    S.dispalySalary()

    print(f"object ID before: {id(S)}")

    increaseSalary(S,3000)
    S.dispalySalary()

    print(f"object ID after: {id(S)}")
main()