from sys import argv
codename,filename = argv
f=open(filename,"r")
print(f.read())
f.close()
f=open(filename,"a")
f.write("\nAIT2609028")
f.close() 
#print(argv)