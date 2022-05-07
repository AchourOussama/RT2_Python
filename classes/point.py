import math
class Point:
    def __init__(self,abscissa,ordinate) :
        self.abscissa=abscissa
        self.ordinate=ordinate
    def distance(self,point:object):
        diffX=self.abscissa-point.abscissa
        diifY=self.ordinate-point.ordinate
        return math.sqrt(math.pow(diffX,2)+math.pow(diifY,2))
    def showCoordinates(self):
        print("abcissa: {}\nordinate{}".format(self.abscissa,self.ordinate))
    def __eq__(self, __o: object):

        if (self.abscissa==__o.abscissa and self.ordinate==__o.ordinate   ) :
            return True
        return False

class ColoredPoint(Point):
    def __init__(self, abscissa, ordinate,r,g,b):
        super().__init__(abscissa, ordinate)
        self.r=r
        self.g=g
        self.b=b

class Polygonne:
    def __init__(self,*points:object) :
        self.points=points
    def perimeter(self):
        per=0 
        for i in range(len(self.points)):
            if i == len(self.points)-1:
                per+=self.points[i].distance(self.points[0])
                return per
            per+=self.points[i].distance(self.points[i+1])

# p1=Point(5,1)
# p2=Point(1,-2)
# p3=Point(5,1)
# print(p1.distance(p2))
# print(p1.__eq__(p3))