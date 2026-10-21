from sys import argv

work,file=argv
 
line1=input("Please enter your name: ")
line2=input("Please enter your age: ")
line3=input("please enter yuor ID: ")

with open(file,'w') as document:
    document.write(line1+'\n')
    document.write(line2+'\n')
    document.write(line3+'\n')
document.close()

with open(file, 'r') as document:
    print(document.read())
