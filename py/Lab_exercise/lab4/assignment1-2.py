Hours=int(input("Please enter your work hours: "))
if Hours<=160:
    salary=Hours*10
    print(f"Your salary is {salary} dollars.")
else:
    salary=(Hours-160)*10*4+1600
    print(f"Your salary is {salary} dollars.")