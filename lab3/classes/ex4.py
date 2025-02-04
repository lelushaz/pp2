import math
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def show(self):
        print(self.x,self.y)

    def move(self,x2,y2):
        self.x=x2
        self.y=y2

    def dist(self, Point):
        return int(math.sqrt((self.x - Point.x)**2 + (self.y - Point.y)**2))
    
point1=Point(int(input()), int(input()))
point2=Point(int(input()), int(input()))
point1.show()
point2.show()
point1.move(7, 5)
point2.move(5, 7)
print(point1.dist(point2))