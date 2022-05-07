import point

p1=point.Point(0,1)
p2=point.Point(1,0)
p3=point.Point(0,-1)
p4=point.Point(-1,0)

poly=point.Polygonne(p1,p2,p3,p4)
print("perimeter: ",poly.perimeter())
print(point.Point.__dict__)