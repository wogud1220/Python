class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
 
p1 = Point2D(x=30, y=20)    # 점1
p2 = Point2D(x=60, y=50)    # 점2
p3 = Point2D(x=30, y=40)    # 점3
 
print('p1: {} {}'.format(p1.x, p1.y))    # 30 20
print('p2: {} {}'.format(p2.x, p2.y))    # 60 50
print('p3: {} {}'.format(p3.x, p3.y))    # 30 40
