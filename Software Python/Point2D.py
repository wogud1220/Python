import math

class Point2D():
    def __init__(self, x, y):
        self.x= x
        self.y=y
    def print(self):
        print("(X, Y) =", self.x, self.y)
    def distanceTo(self, point):
        dx = self.x - point.x
        dy = self.y - point.y
        return math.sqrt(dx*dx + dy*dy)

class Point3D(Point2D): 
    def __init__(self, x, y, z):
        super().__init__(x,y)
        self.z=z
    def print(self):
        print("(X, Y, z) = ", self.x, self.y, self.z)
    def distance(self, point):
        dx =self.x - point.x
        dy =self.y - point.y
        dz =self.z - point.z
        return math.sqrt(dx*dx + dy * dy + dz * dz)
class Point4D(Point3D):
    def __init__(self, x, y, z, w):
        super().__init__(x,y,z)
        self.w=w
    def print(self):
        print("(X, Y, Z, W) =", self.x, self.y, self.z, self.w)
    def distanceTo(self, point):
        dx = self.x - point.x
        