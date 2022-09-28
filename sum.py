import math

class Triangle(Point2D):
    def __init__(self, p1, p2, p3):
        self.p1 =p1
        self.p2 =p2
        self.p3 =p3
    def area(self):
        x1= self.p1.x
        y1= self.p1.y
        x2= self.p2.x
        y2= self.p2.y
        x3= self.p3.x
        y3= self.p3.y
        return 0.5*abs((x1*y2 + x2*y3+ x3*y1)-(x1*y3 + x3*y2 + x2*y1))
p1 = Triangle(x1=15, y1=25)
p2 = Triangle(x2=30, y2=55)
p3 = Triangle(x3=50, y3=75)

tri = Triangle(p1, p2, p3)
print(tri.area)