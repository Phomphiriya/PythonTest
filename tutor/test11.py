class rectangle:
    def __init__(self,width = None ,height = None):
        if width == None:
            self.width = "Empty width"
        else:
            self.width = width
        
        if height == None:
            self.height = "Empty height"
        else:
            self.height = height

    def getArea(self):
        return round(int(self.width * self.height),2)

    def __str__(self):
        return "{} {}".format(self.width,self.height)
    
width,height = input("Enter W,H : ").split(',')
width = int(width)
height = int(height)
r = rectangle(width,height)

print(r)
print(r.getArea())