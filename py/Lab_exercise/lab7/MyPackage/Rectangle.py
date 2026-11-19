class rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def GetArea(self):
            return self.width*self.height
        
    def GetPerimeter(self):
        return 2*(self.width+self.height)