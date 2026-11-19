class Rectangle:
    def __init__(self,width=1,height=1):
        self.width=width
        self.height=height

    def GetArea(self):
        return self.width*self.height
    
    def GetPerimeter(self):
        return 2*(self.width+self.height)
    
    def setDimensions(self,width,height):
        self.width=width
        self.height=height

def main():
    R1=Rectangle(5,10)
    R2=Rectangle(2,4)
    
    print("Area of R1: ",R1.GetArea())
    print("Perimeter of R1: ",R1.GetPerimeter())
    print("Area of R2: ",R2.GetArea())
    print("Perimeter of R2: ",R2.GetPerimeter())

    R1.setDimensions(3,6)
    print("New area of R1: ",R1.GetArea())
    print("New perimeter of R1: ",R1.GetPerimeter())

main()