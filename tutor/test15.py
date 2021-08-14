import math

class Circle:
    def __init__(self,radius,color=None):

        self.radius = radius
        if color == None:
            self.color = "White"
        else:
            self.color = color
    
    def findArea(self):
        area = 2*math.pi*self.radius
        return round(area,2)
    
    def __str__(self):
        return str("This {} circle radius = {}").format(self.color,self.findArea())

inp = list(input("Enter input : ").split())
c = Circle(int(inp[0]),inp[1])
print(c)